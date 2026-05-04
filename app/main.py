from __future__ import annotations

import time
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markdown_it import MarkdownIt

from app import db, reddit

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
md = MarkdownIt("commonmark", {"breaks": True, "linkify": True})

app = FastAPI(title="r/nosleep time machine")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


def fmt_date(ts: int) -> str:
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%b %d, %Y")


def fmt_month(ts: int) -> str:
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%b %Y")


templates.env.filters["fmt_date"] = fmt_date
templates.env.filters["fmt_month"] = fmt_month


@app.get("/healthz", response_class=PlainTextResponse)
def healthz() -> str:
    return "ok"


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    db.init_schema()
    mn, mx = db.date_bounds()
    default_after = max(mn, mx - 86400 * 365)
    default_before = mx
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "min_ts": mn,
            "max_ts": mx,
            "default_after": default_after,
            "default_before": default_before,
        },
    )


@app.get("/api/top", response_class=HTMLResponse)
def api_top(
    request: Request,
    after: int = Query(..., ge=0),
    before: int = Query(..., ge=0),
    limit: int = Query(25, ge=1, le=100),
) -> HTMLResponse:
    if before < after:
        after, before = before, after
    rows = db.top_in_window(after, before, limit)
    return templates.TemplateResponse(
        request,
        "_results.html",
        {
            "posts": rows,
            "after": after,
            "before": before,
            "limit": limit,
            "count": len(rows),
        },
    )


@app.get("/post/{post_id}", response_class=HTMLResponse)
async def reader(
    request: Request,
    post_id: str,
    after: int | None = None,
    before: int | None = None,
) -> HTMLResponse:
    row = db.get_post(post_id)
    if row is None:
        raise HTTPException(status_code=404, detail="post not in local archive")

    selftext = row["selftext"]
    if not selftext:
        fetched = await reddit.fetch_selftext(post_id)
        if fetched:
            db.update_selftext(post_id, fetched)
            selftext = fetched

    body_html = md.render(selftext) if selftext else ""
    back_qs = ""
    if after is not None and before is not None:
        back_qs = f"?after={after}&before={before}"

    return templates.TemplateResponse(
        request,
        "reader.html",
        {
            "post": row,
            "body_html": body_html,
            "has_body": bool(selftext),
            "back_qs": back_qs,
        },
    )
