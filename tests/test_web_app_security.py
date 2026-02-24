from __future__ import annotations

from pathlib import Path

import pytest

pytest.importorskip("flask")

from labs.lab06_mock_web_vulnerability.app import create_app


def test_insecure_mode_allows_sql_injection_simulation(tmp_path: Path) -> None:
    db_path = tmp_path / "lab06_insecure.sqlite3"
    app = create_app(mode="insecure", database_path=str(db_path))
    client = app.test_client()

    resp = client.get("/search?q=' OR '1'='1")
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload["mode"] == "insecure"
    assert payload["count"] >= 2
    assert "SELECT username" in payload["query"]


def test_secure_mode_rejects_unsafe_input_and_allows_safe_query(tmp_path: Path) -> None:
    db_path = tmp_path / "lab06_secure.sqlite3"
    app = create_app(mode="secure", database_path=str(db_path))
    client = app.test_client()

    bad = client.get("/search?q=' OR '1'='1")
    assert bad.status_code == 400
    bad_payload = bad.get_json()
    assert bad_payload["mode"] == "secure"
    assert "Invalid username format" in bad_payload["error"]

    good = client.get("/search?q=alice")
    assert good.status_code == 200
    good_payload = good.get_json()
    assert good_payload["count"] == 1
    assert good_payload["results"][0]["username"] == "alice"
