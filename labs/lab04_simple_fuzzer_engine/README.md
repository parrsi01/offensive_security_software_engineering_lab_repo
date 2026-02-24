# Lab04: Simple Fuzzer Engine (Python)

Author: Simon Parris  
Generated: 2026-02-24

## Concept Overview
This lab builds a small mutation-based fuzzer in Python. It mutates seed inputs, executes a local target function, logs crashes, and writes a summary report. The design is intentionally simple so learners can understand the full execution loop.

## Threat Model
- Asset: parser robustness and crash resistance in local components
- Attacker capability: can send malformed input to a parser
- Unsafe condition: unhandled exceptions / parser assumptions
- Impact: crashes, service instability, denial-of-service conditions
- Training scope: local Python functions only

## Step-by-Step CLI Instructions
```bash
cd labs/lab04_simple_fuzzer_engine
PYTHONPATH=../.. python3 fuzzer.py --target crash_on_magic --iterations 25 --seed-corpus sample_seed.txt
```

## VS Code Workflow Instructions
1. Open `fuzzer.py` and `targets.py`.
2. Run the fuzzer from the integrated terminal.
3. Open `artifacts/crashes/` and `artifacts/reports/summary.json` after execution.
4. Change mutation strategies and rerun to compare coverage behavior.

## Expected Output
- JSON summary printed to stdout
- `artifacts/reports/summary.json` created
- At least one crash file when seed corpus includes `CRASHME`

## Common Debugging Errors
- `ModuleNotFoundError: labs`: set `PYTHONPATH` to the repository root.
- No crashes found: use `sample_seed.txt` or increase iterations.
- Permission errors writing artifacts: ensure the lab directory is writable.

## Secure Rewrite
The secure engineering outcome is not “remove fuzzing”; it is to harden the target:
- validate input structure before parsing
- handle parser exceptions safely
- add regression tests for each crash reproducer
- enforce timeouts/resource limits in production parsing paths

## Security Implications
Fuzzing is a practical way to find reliability and security issues early in development. Even lightweight fuzzers improve engineering feedback loops.

## Professional Skill Alignment
- Junior Vulnerability Researcher: crash discovery and reproducer capture
- Security R&D Engineer: tooling automation and corpus mutation design
- Security Software Engineer: parser hardening from crash evidence
