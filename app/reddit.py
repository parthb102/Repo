"""Lazy fallback to fetch selftext directly from Reddit when missing from the dump."""

from __future__ import annotations

import logging

import httpx

USER_AGENT = "nosleep-reader/0.1 (local personal reader)"
log = logging.getLogger(__name__)


async def fetch_selftext(post_id: str) -> str | None:
    url = f"https://www.reddit.com/comments/{post_id}.json?raw_json=1&limit=1"
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as client:
            r = await client.get(url, headers=headers)
            r.raise_for_status()
            data = r.json()
    except Exception as e:
        log.warning("reddit fetch failed for %s: %s", post_id, e)
        return None

    try:
        post = data[0]["data"]["children"][0]["data"]
    except (KeyError, IndexError, TypeError):
        return None

    body = post.get("selftext")
    if body in (None, "", "[removed]", "[deleted]"):
        return None
    return body
