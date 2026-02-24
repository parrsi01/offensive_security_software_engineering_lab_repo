from __future__ import annotations


def crash_on_magic(data: bytes) -> None:
    """Intentionally raises on a magic token for deterministic fuzz lab testing."""
    if b"CRASHME" in data:
        raise RuntimeError("Simulated crash: magic token reached")
    if data.startswith(b"LEN") and len(data) > 32:
        raise ValueError("Simulated parser overflow path")


def parse_kv_pairs(data: bytes) -> None:
    text = data.decode("utf-8", errors="ignore")
    for pair in text.split(";"):
        if not pair:
            continue
        if "=" not in pair:
            raise ValueError(f"Malformed pair: {pair!r}")
        key, value = pair.split("=", 1)
        if not key:
            raise ValueError("Empty key")
        if len(value) > 128:
            raise ValueError("Value too long")


def safe_noop(data: bytes) -> None:
    _ = len(data)
