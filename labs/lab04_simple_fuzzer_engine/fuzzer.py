from __future__ import annotations

import argparse
import json
import random
import string
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Iterable, List, Sequence

from labs.lab04_simple_fuzzer_engine import targets

TargetFunc = Callable[[bytes], None]


@dataclass
class CrashRecord:
    iteration: int
    exception_type: str
    message: str
    input_hex: str
    input_preview: str


@dataclass
class FuzzSummary:
    target: str
    iterations: int
    crashes: int
    crash_files: List[str]
    seed: int
    duration_ms: int


def _mutate(data: bytes, rng: random.Random) -> bytes:
    if not data:
        data = b"A"
    buf = bytearray(data)
    strategy = rng.choice(["flip", "insert", "delete", "append"])
    if strategy == "flip" and buf:
        idx = rng.randrange(len(buf))
        buf[idx] = rng.randrange(0, 256)
    elif strategy == "insert":
        idx = rng.randrange(len(buf) + 1)
        buf[idx:idx] = bytes([rng.randrange(0, 256)])
    elif strategy == "delete" and buf:
        idx = rng.randrange(len(buf))
        del buf[idx]
    else:
        buf.extend(rng.choice(string.ascii_letters).encode())
    return bytes(buf[:256])


def _write_crash(out_dir: Path, record: CrashRecord) -> str:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"crash_iter_{record.iteration}.json"
    path.write_text(json.dumps(asdict(record), indent=2), encoding="utf-8")
    return str(path)


def load_seed_corpus(seed_corpus_path: str | None) -> List[bytes]:
    if not seed_corpus_path:
        return [b"A", b"test=1", b"LEN:hello"]
    corpus = []
    for line in Path(seed_corpus_path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        corpus.append(line.encode("utf-8"))
    return corpus or [b"A"]


def get_target(name: str) -> TargetFunc:
    mapping = {
        "crash_on_magic": targets.crash_on_magic,
        "parse_kv_pairs": targets.parse_kv_pairs,
        "safe_noop": targets.safe_noop,
    }
    if name not in mapping:
        raise KeyError(f"Unknown target: {name}")
    return mapping[name]


def run_fuzz_session(
    target_name: str,
    iterations: int,
    out_dir: str,
    seed_corpus: Sequence[bytes] | None = None,
    random_seed: int = 1337,
) -> FuzzSummary:
    rng = random.Random(random_seed)
    start = time.time()
    crash_dir = Path(out_dir) / "crashes"
    report_dir = Path(out_dir) / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    target = get_target(target_name)
    corpus = list(seed_corpus or [b"A"])
    crash_files: List[str] = []

    initial_corpus_count = len(corpus)
    for iteration in range(iterations):
        if iteration < initial_corpus_count:
            candidate = corpus[iteration]
        else:
            base = rng.choice(corpus)
            candidate = _mutate(base, rng)
        try:
            target(candidate)
            if len(candidate) <= 128:
                corpus.append(candidate)
        except Exception as exc:  # noqa: BLE001 - intentional for crash capture
            record = CrashRecord(
                iteration=iteration,
                exception_type=type(exc).__name__,
                message=str(exc),
                input_hex=candidate.hex(),
                input_preview=candidate[:32].decode("utf-8", errors="replace"),
            )
            crash_files.append(_write_crash(crash_dir, record))
            corpus.append(candidate)

    duration_ms = int((time.time() - start) * 1000)
    summary = FuzzSummary(
        target=target_name,
        iterations=iterations,
        crashes=len(crash_files),
        crash_files=crash_files,
        seed=random_seed,
        duration_ms=duration_ms,
    )
    (report_dir / "summary.json").write_text(json.dumps(asdict(summary), indent=2), encoding="utf-8")
    return summary


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Simple educational fuzzer engine")
    parser.add_argument("--target", default="crash_on_magic")
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--seed", type=int, default=1337)
    parser.add_argument("--seed-corpus", default=None)
    parser.add_argument("--out-dir", default=str(Path(__file__).resolve().parent / "artifacts"))
    args = parser.parse_args(list(argv) if argv is not None else None)

    corpus = load_seed_corpus(args.seed_corpus)
    summary = run_fuzz_session(
        target_name=args.target,
        iterations=args.iterations,
        out_dir=args.out_dir,
        seed_corpus=corpus,
        random_seed=args.seed,
    )
    print(json.dumps(asdict(summary), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
