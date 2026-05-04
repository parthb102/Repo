# r/nosleep time machine

A small local app for reading top r/nosleep stories from any time window — drag a
date-range slider, see the top stories that ranked in that window, click into a
clean reader view.

Historical post metadata comes from [Arctic Shift](https://arctic-shift.photon-reddit.com)
(community-maintained successor to Pushshift). Story bodies are pulled from the
dump where available, with a lazy fallback to Reddit's own JSON endpoint for
posts whose body wasn't archived.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

## Ingest

Populate the local SQLite archive (`data/posts.sqlite`). Resumable — re-running
skips months already complete.

```bash
# Quick sanity check (one month):
python ingest.py --from 2014-10 --to 2014-10

# Full archive (2010-05 → today, top 100/month). Takes ~30 min.
python ingest.py
```

Useful flags:

- `--from YYYY-MM` / `--to YYYY-MM` — limit the range
- `--top-n N` — top N per month (max 100, default 100)
- `--refresh` — force re-ingest of months already marked complete
- `--sleep 0.3` — seconds between API calls
- `-v` — verbose logging

## Run

```bash
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000.

## How it works

- `ingest.py` walks months 2010-05 → now and pulls top-100 posts/month from
  Arctic Shift into `posts.sqlite`.
- `app/main.py` serves the slider UI. Drag the handles → HTMX hits
  `/api/top?after=…&before=…&limit=…` → SQL query against the local cache →
  rendered post list swaps in.
- `/post/{id}` renders the story body as markdown. If `selftext` is missing
  from the dump, it lazy-fetches from `reddit.com/comments/{id}.json` and
  caches it back into SQLite.

## Schema

```
posts(id PK, title, author, created_utc, score, num_comments,
      permalink, url, selftext, flair, fetched_at)
ingest_state(month PK 'YYYY-MM', completed_at)
```

Top-in-window query:

```sql
SELECT * FROM posts
 WHERE created_utc BETWEEN ? AND ?
 ORDER BY score DESC LIMIT ?;
```
