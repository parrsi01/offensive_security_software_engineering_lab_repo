from __future__ import annotations

import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request


def create_app(mode: str = "vulnerable") -> Flask:
    app = Flask(__name__)
    db_path = Path(__file__).resolve().parent / "mobile_backend.sqlite3"

    def reset_db() -> None:
        conn = sqlite3.connect(db_path)
        try:
            conn.execute("CREATE TABLE IF NOT EXISTS sessions (user_id TEXT, token TEXT)")
            conn.execute("DELETE FROM sessions")
            conn.executemany(
                "INSERT INTO sessions(user_id, token) VALUES (?, ?)",
                [("u100", "tok-alice"), ("u200", "tok-bob")],
            )
            conn.commit()
        finally:
            conn.close()

    reset_db()

    @app.get("/session")
    def get_session():
        user_id = request.args.get("user_id", "")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            if mode == "vulnerable":
                sql = f"SELECT user_id, token FROM sessions WHERE user_id = '{user_id}'"
                rows = conn.execute(sql).fetchall()
                return jsonify({"mode": mode, "query": sql, "results": [dict(r) for r in rows]})
            rows = conn.execute(
                "SELECT user_id, token FROM sessions WHERE user_id = ?",
                (user_id,),
            ).fetchall()
            return jsonify({"mode": mode, "results": [dict(r) for r in rows]})
        finally:
            conn.close()

    return app


if __name__ == "__main__":  # pragma: no cover
    create_app().run(host="127.0.0.1", port=5050, debug=False)
