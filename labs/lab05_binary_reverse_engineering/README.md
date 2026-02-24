# Lab05: Binary Reverse Engineering (objdump-first Workflow)

Author: Simon Parris  
Generated: 2026-02-24

## Concept Overview
This lab compiles a small C binary and walks through a source-assisted reverse engineering process using `objdump`. Learners reconstruct control flow and identify comparison logic without modifying the binary.

## Threat Model
- Asset: code understanding and trust boundaries in compiled software
- Attacker capability (training context): analyst can inspect a local binary
- Unsafe condition: opaque logic / hidden checks that are difficult to audit
- Impact: insecure assumptions, difficult patching, weak review coverage
- Training scope: local analysis only

## Step-by-Step CLI Instructions
```bash
cd labs/lab05_binary_reverse_engineering
bash build_and_disassemble.sh
./build/challenge test1234 || true
python3 reconstruct_logic.py
```

## VS Code Workflow Instructions
1. Open `challenge.c` and `build/challenge.objdump.txt` side-by-side.
2. Search for `<main>` and `<score_input>` in the disassembly.
3. Trace branch instructions (`cmp`, `je`, `jne`) and map them to source checks.

## Expected Output
- Compiled binary and objdump text file
- Program prints a score and `ACCESS: denied` for most inputs
- `reconstruct_logic.py` extracts key disassembly lines for review notes

## Common Debugging Errors
- `objdump: command not found`: install `binutils`.
- Missing `build/challenge.objdump.txt`: run `build_and_disassemble.sh` first.
- Disassembly differs from README examples: compiler/version changes can reorder instructions.

## Secure Rewrite
Security engineering improvements for production code:
- avoid security decisions based on hidden client-side checks
- move access control decisions to a trusted service boundary
- document algorithms and validation rules for auditability

## Security Implications
Reverse engineering skills help defenders validate what binaries actually do, not just what source comments claim they do.

## Professional Skill Alignment
- Reverse Engineering Analyst: disassembly reading and logic reconstruction
- Application Security Engineer: trust-boundary review for compiled artifacts
- Security Software Engineer: design for auditable control flow
