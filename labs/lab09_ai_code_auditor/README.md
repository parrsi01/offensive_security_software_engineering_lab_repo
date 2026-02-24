# Lab09: AI-Assisted Code Auditor CLI (Pattern-Based Training Tool)

Author: Simon Parris  
Generated: 2026-02-24

## Concept Overview
This lab provides a local CLI scanner that flags insecure code patterns and prints secure rewrite suggestions. It is called “AI-assisted” because it mirrors the triage workflow often automated before human review, but the implementation here is deterministic and offline (regex/pattern based).

## Threat Model
- Asset: codebase security posture and review coverage
- Attacker capability: introduces insecure coding patterns into source files
- Unsafe condition: risky APIs and shell/SQL anti-patterns remain unreviewed
- Impact: memory corruption, command injection, SQL injection, audit gaps
- Training scope: local files only; no cloud services

## Step-by-Step CLI Instructions
```bash
cd labs/lab09_ai_code_auditor
PYTHONPATH=../.. python3 auditor.py sample_targets
bash run_demo.sh
```

## VS Code Workflow Instructions
1. Open `patterns.py`, `auditor.py`, and `sample_targets/insecure_demo.c`.
2. Run the auditor in the integrated terminal.
3. Add another insecure line (e.g., `gets(`) and rerun to see a new finding.
4. Replace with a secure pattern and confirm the finding disappears.

## Expected Output
- Text report listing file count and findings
- `c_strcpy` finding on `sample_targets/insecure_demo.c`
- Secure rewrite suggestion text for each finding

## Common Debugging Errors
- `ModuleNotFoundError: labs`: set `PYTHONPATH` to repo root.
- No findings when expected: ensure file extensions are supported and pattern text matches regex assumptions.
- JSON serialization issues after extending the schema: keep dataclasses serializable.

## Secure Rewrite
The auditor itself suggests safer alternatives, but secure engineering requires follow-through:
- patch the code
- add regression tests
- rerun scanner and functional tests
- require review gates in CI (future extension)

## Security Implications
Pattern scanners improve baseline coverage quickly, but they are not a substitute for code review, threat modeling, or dynamic testing.

## Professional Skill Alignment
- Security Software Engineer: security tooling development
- Application Security Engineer: triage automation and review augmentation
- Security R&D Engineer: rule design and false-positive tuning
