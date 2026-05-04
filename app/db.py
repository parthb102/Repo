import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "posts.sqlite"

SCHEMA = """
CREATE TABLE IF NOT EXISTS posts (
    id           TEXT PRIMARY KEY,
    title        TEXT NOT NULL,
    author       TEXT,
    created_utc  INTEGER NOT NULL,
    score        INTEGER NOT NULL,
    num_comments INTEGER,
    permalink    TEXT NOT NULL,
    url          TEXT,
    selftext     TEXT,
    flair        TEXT,
    fetched_at   INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_posts_created ON posts(created_utc);
CREATE INDEX IF NOT EXISTS idx_posts_score   ON posts(score DESC);

CREATE TABLE IF NOT EXISTS ingest_state (
    month        TEXT PRIMARY KEY,
    completed_at INTEGER NOT NULL
);
"""


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_schema() -> None:
    with connect() as conn:
        conn.executescript(SCHEMA)


@contextmanager
def cursor():
    conn = connect()
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def upsert_post(conn: sqlite3.Connection, row: dict) -> None:
    conn.execute(
        """
        INSERT INTO posts (id, title, author, created_utc, score, num_comments,
                           permalink, url, selftext, flair, fetched_at)
        VALUES (:id, :title, :author, :created_utc, :score, :num_comments,
                :permalink, :url, :selftext, :flair, :fetched_at)
        ON CONFLICT(id) DO UPDATE SET
            title        = excluded.title,
            author       = excluded.author,
            score        = excluded.score,
            num_comments = excluded.num_comments,
            permalink    = excluded.permalink,
            url          = excluded.url,
            selftext     = COALESCE(excluded.selftext, posts.selftext),
            flair        = excluded.flair,
            fetched_at   = excluded.fetched_at
        """,
        row,
    )


def mark_month_done(conn: sqlite3.Connection, month: str) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO ingest_state(month, completed_at) VALUES (?, ?)",
        (month, int(time.time())),
    )


def month_is_done(conn: sqlite3.Connection, month: str) -> bool:
    row = conn.execute(
        "SELECT 1 FROM ingest_state WHERE month = ?", (month,)
    ).fetchone()
    return row is not None


def top_in_window(after: int, before: int, limit: int = 25) -> list[sqlite3.Row]:
    with connect() as conn:
        return conn.execute(
            """
            SELECT id, title, author, created_utc, score, num_comments, permalink, flair
            FROM posts
            WHERE created_utc BETWEEN ? AND ?
            ORDER BY score DESC, created_utc ASC
            LIMIT ?
            """,
            (after, before, limit),
        ).fetchall()


def get_post(post_id: str) -> sqlite3.Row | None:
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM posts WHERE id = ?", (post_id,)
        ).fetchone()


def update_selftext(post_id: str, selftext: str) -> None:
    with connect() as conn:
        conn.execute(
            "UPDATE posts SET selftext = ? WHERE id = ?", (selftext, post_id)
        )
        conn.commit()


def date_bounds() -> tuple[int, int]:
    with connect() as conn:
        row = conn.execute(
            "SELECT MIN(created_utc) AS mn, MAX(created_utc) AS mx FROM posts"
        ).fetchone()
        if row is None or row["mn"] is None:
            now = int(time.time())
            return now - 86400 * 30, now
        return int(row["mn"]), int(row["mx"])
