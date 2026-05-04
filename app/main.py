from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, abort, render_template, request
from markdown_it import MarkdownIt

from app import db, reddit

BASE_DIR = Path(__file__).resolve().parent
app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)
md = MarkdownIt("commonmark", {"breaks": True, "linkify": True})


def fmt_date(ts: int) -> str:
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%b %d, %Y")


def fmt_month(ts: int) -> str:
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%b %Y")


app.jinja_env.filters["fmt_date"] = fmt_date
app.jinja_env.filters["fmt_month"] = fmt_month


@app.get("/healthz")
def healthz() -> str:
    return "ok"


@app.get("/")
def index():
    db.init_schema()
    mn, mx = db.date_bounds()
    default_after = max(mn, mx - 86400 * 365)
    default_before = mx
    return render_template(
        "index.html",
        min_ts=mn,
        max_ts=mx,
        default_after=default_after,
        default_before=default_before,
    )


@app.get("/api/top")
def api_top():
    try:
        after = int(request.args.get("after", "0"))
        before = int(request.args.get("before", "0"))
        limit = int(request.args.get("limit", "25"))
    except ValueError:
        abort(400)
    limit = max(1, min(limit, 100))
    if before < after:
        after, before = before, after
    rows = db.top_in_window(after, before, limit)
    return render_template(
        "_results.html",
        posts=rows,
        after=after,
        before=before,
        limit=limit,
        count=len(rows),
    )


@app.get("/post/<post_id>")
def reader(post_id: str):
    row = db.get_post(post_id)
    if row is None:
        abort(404, description="post not in local archive")

    selftext = row["selftext"]
    if not selftext:
        fetched = reddit.fetch_selftext(post_id)
        if fetched:
            db.update_selftext(post_id, fetched)
            selftext = fetched

    body_html = md.render(selftext) if selftext else ""
    after = request.args.get("after")
    before = request.args.get("before")
    back_qs = f"?after={after}&before={before}" if after and before else ""

    return render_template(
        "reader.html",
        post=row,
        body_html=body_html,
        has_body=bool(selftext),
        back_qs=back_qs,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
