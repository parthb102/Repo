"""Ingest top r/nosleep posts per month from Arctic Shift into local SQLite.

Resumable: re-running skips months already recorded in `ingest_state`.
Use --refresh to force re-ingest of a month range.
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from datetime import datetime, timezone

import httpx
from dateutil.relativedelta import relativedelta

from app import db

ARCTIC = "https://arctic-shift.photon-reddit.com/api/posts/search"
SUBREDDIT = "nosleep"
SUBREDDIT_BIRTH = datetime(2010, 5, 1, tzinfo=timezone.utc)
USER_AGENT = "nosleep-reader/0.1 (local personal reader)"

log = logging.getLogger("ingest")


def month_iter(start: datetime, end: datetime):
    cur = start.replace(day=1)
    end = end.replace(day=1)
    while cur <= end:
        nxt = cur + relativedelta(months=1)
        yield cur, nxt
        cur = nxt


def parse_month(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m").replace(tzinfo=timezone.utc)


def fetch_month(client: httpx.Client, after: int, before: int, limit: int) -> list[dict]:
    params = {
        "subreddit": SUBREDDIT,
        "after": after,
        "before": before,
        "sort": "desc",
        "limit": limit,
    }
    for attempt in range(5):
        r = client.get(ARCTIC, params=params, headers={"User-Agent": USER_AGENT}, timeout=60)
        if r.status_code == 429:
            reset = int(r.headers.get("X-RateLimit-Reset", "5"))
            log.warning("rate-limited; sleeping %ds", reset)
            time.sleep(max(1, reset))
            continue
        r.raise_for_status()
        payload = r.json()
        if isinstance(payload, dict):
            return payload.get("data", [])
        if isinstance(payload, list):
            return payload
        return []
    raise RuntimeError("exhausted retries on rate limit")


def normalize(rec: dict, fetched_at: int) -> dict | None:
    pid = rec.get("id")
    title = rec.get("title")
    created = rec.get("created_utc")
    if not pid or not title or created is None:
        return None
    permalink = rec.get("permalink") or f"/r/nosleep/comments/{pid}/"
    if permalink and not permalink.startswith("http"):
        permalink = "https://www.reddit.com" + permalink
    selftext = rec.get("selftext")
    if selftext in ("", "[removed]", "[deleted]"):
        selftext = None
    return {
        "id": pid,
        "title": title,
        "author": rec.get("author"),
        "created_utc": int(created),
        "score": int(rec.get("score") or 0),
        "num_comments": int(rec.get("num_comments") or 0),
        "permalink": permalink,
        "url": rec.get("url"),
        "selftext": selftext,
        "flair": rec.get("link_flair_text"),
        "fetched_at": fetched_at,
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--from", dest="start", default="2010-05",
                   help="start month YYYY-MM (default: 2010-05)")
    p.add_argument("--to", dest="end", default=None,
                   help="end month YYYY-MM inclusive (default: current month)")
    p.add_argument("--top-n", type=int, default=100,
                   help="top N per month (default 100, max 100)")
    p.add_argument("--refresh", action="store_true",
                   help="re-ingest months already marked complete")
    p.add_argument("--sleep", type=float, default=0.3,
                   help="seconds between API calls (default 0.3)")
    p.add_argument("-v", "--verbose", action="store_true")
    args = p.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    start = max(parse_month(args.start), SUBREDDIT_BIRTH)
    end = parse_month(args.end) if args.end else datetime.now(timezone.utc).replace(day=1)
    limit = min(max(args.top_n, 1), 100)

    db.init_schema()

    total_posts = 0
    total_months = 0
    with httpx.Client(http2=False) as client:
        for cur, nxt in month_iter(start, end):
            month_key = cur.strftime("%Y-%m")
            with db.cursor() as conn:
                if not args.refresh and db.month_is_done(conn, month_key):
                    log.debug("skip %s (already ingested)", month_key)
                    continue

            after = int(cur.timestamp())
            before = int(nxt.timestamp()) - 1
            try:
                records = fetch_month(client, after, before, limit)
            except Exception as e:
                log.error("fetch failed for %s: %s", month_key, e)
                continue

            now = int(time.time())
            inserted = 0
            with db.cursor() as conn:
                for rec in records:
                    norm = normalize(rec, now)
                    if norm is None:
                        continue
                    db.upsert_post(conn, norm)
                    inserted += 1
                db.mark_month_done(conn, month_key)

            total_posts += inserted
            total_months += 1
            log.info("%s: %d posts (top score %d)",
                     month_key, inserted,
                     max((int(r.get("score") or 0) for r in records), default=0))
            time.sleep(args.sleep)

    log.info("done: %d months, %d posts", total_months, total_posts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
