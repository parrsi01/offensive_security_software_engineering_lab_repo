# Offensive Security Software Engineering Lab

Author: Simon Parris  
Generated: 2026-02-24

## Ethical Disclaimer (Required)
This repository is a safe, education-focused vulnerability research and exploit engineering lab. Every vulnerable program is intentionally created for training, runs only in a Linux VM or Docker container, and includes secure remediation guidance. It must not be used against systems you do not own or administer with explicit written authorization.

## Purpose
This lab teaches junior vulnerability researchers and security software engineers how to analyze intentionally vulnerable code, reproduce controlled failures, build small security tools, document findings professionally, and implement secure remediations.

## Professional Role Alignment
- Junior Vulnerability Researcher
- Security Software Engineer
- Reverse Engineering Analyst
- Application Security Engineer
- Offensive Security Engineer (Legal Context)
- Security R&D Engineer

## Environment Requirements
- Ubuntu Linux VM (recommended)
- VS Code integrated terminal
- Python 3.11+ (tested with 3.12)
- GCC toolchain
- Docker (for container labs)
- Optional: gdb, radare2, tcpdump, objdump
- CLI-only workflow (Codex or Claude CLI friendly)

## Quick Start (Recommended)
```bash
cd offensive_security_engineering_lab
bash tools/install_all_tools.sh --python-only
source .venv/bin/activate
pytest -q tests
```

## GitHub Viewing Notes
- All documentation is Markdown and uses relative paths so it renders cleanly on GitHub.
- Labs are organized by folder with a dedicated `README.md` per lab.
- Build outputs and local environments are git-ignored (see `.gitignore`) so the repository stays readable online.

## Table of Contents
- [Course Overview](#course-overview)
- [Repository Layout](#repository-layout)
- [Lab Index](#lab-index)
- [Setup and Verification](#setup-and-verification)
- [VS Code Workflow](#vs-code-workflow)
- [Testing Policy](#testing-policy)
- [Safety Rules (Operational)](#safety-rules-operational)
- [Capstone Deliverables](#capstone-deliverables)
- [Offline Learning Resources](#offline-learning-resources)
- [GitHub Publishing Checklist](#github-publishing-checklist)

## Course Overview
- `COURSE_OVERVIEW.md`: learning outcomes and competency map
- `ROADMAP.md`: phase-by-phase progression plan
- `documentation/`: theory notes for mitigations, sandboxing, and secure platform concepts
- `tools/`: offline reference docs and setup helpers

## Repository Layout
- `README.md`: master guide, legal scope, setup, execution workflow
- `COURSE_OVERVIEW.md`: learning model and competency map
- `ROADMAP.md`: staged progression and assessment milestones
- `tools/`: installer, cheatsheets, debugger references, offline learning aids
- `labs/`: nine reproducible labs with vulnerable + remediated workflows
- `tests/`: unit/integration tests validating vulnerabilities and remediations
- `documentation/`: theory notes (ASLR/NX, mitigations, sandboxing, etc.)
- `capstone/`: mock mobile backend audit scenario, report template, remediation patch

## Lab Index
1. [`labs/lab01_stack_overflow/README.md`](labs/lab01_stack_overflow/README.md) - Intentional stack overwrite simulation, protected vs unprotected builds, secure rewrite
2. [`labs/lab02_memory_corruption_suite/README.md`](labs/lab02_memory_corruption_suite/README.md) - Format string, integer overflow, and use-after-free lifecycle simulation
3. [`labs/lab03_linux_sandbox_simulation/README.md`](labs/lab03_linux_sandbox_simulation/README.md) - Namespace misconfiguration vs hardened isolation attempt
4. [`labs/lab04_simple_fuzzer_engine/README.md`](labs/lab04_simple_fuzzer_engine/README.md) - Python mutation fuzzer with crash logging and summary reports
5. [`labs/lab05_binary_reverse_engineering/README.md`](labs/lab05_binary_reverse_engineering/README.md) - `objdump`-first binary analysis and logic reconstruction
6. [`labs/lab06_mock_web_vulnerability/README.md`](labs/lab06_mock_web_vulnerability/README.md) - Flask SQL injection simulation with secure parameterized fix
7. [`labs/lab07_packet_analysis/README.md`](labs/lab07_packet_analysis/README.md) - `tcpdump` loopback header analysis (with offline sample)
8. [`labs/lab08_container_security/README.md`](labs/lab08_container_security/README.md) - Vulnerable vs hardened Dockerfile comparison
9. [`labs/lab09_ai_code_auditor/README.md`](labs/lab09_ai_code_auditor/README.md) - Offline pattern-based code auditor with secure rewrite hints

## Setup and Verification
### Full Python Setup (Local `.venv`)
```bash
bash tools/install_all_tools.sh --python-only
source .venv/bin/activate
pytest -q tests
```

### OS Tooling (Ubuntu VM)
The installer prints suggested package commands. Recommended packages:
- `build-essential`
- `gdb`
- `binutils`
- `tcpdump`
- `docker.io`
- `python3-venv`

### Smoke Test Commands
```bash
bash labs/lab01_stack_overflow/run_demo.sh
bash labs/lab02_memory_corruption_suite/run_suite.sh
PYTHONPATH=. python3 labs/lab04_simple_fuzzer_engine/fuzzer.py --iterations 25 --seed-corpus labs/lab04_simple_fuzzer_engine/sample_seed.txt
PYTHONPATH=. python3 labs/lab09_ai_code_auditor/auditor.py labs/lab09_ai_code_auditor/sample_targets
```

## VS Code Workflow
1. Open the repository root in VS Code.
2. Open the integrated terminal.
3. Run `bash tools/install_all_tools.sh --python-only`.
4. Activate the virtual environment: `source .venv/bin/activate`.
5. Open the relevant lab `README.md` and source files side-by-side.
6. Run lab commands directly from the terminal.
7. Run targeted tests (for example, `pytest -q tests/test_lab01.py`).

## Testing Policy
The test suite validates vulnerable and remediated behavior in a controlled way:
- Lab01 demonstrates an intentional overwrite condition before fix and rejection after fix.
- Lab04 validates that the fuzzer logs a crash when a seeded crashing input is present.
- Lab06 validates insecure input handling vs secure validation/parameterized query behavior.
- Lab09 validates insecure pattern detection and secure rewrite suggestions.

### Current Test Coverage (Repository)
- `tests/test_lab01.py`
- `tests/test_lab04_fuzzer.py`
- `tests/test_lab09_ai_auditor.py`
- `tests/test_web_app_security.py`

## Capstone Deliverables
- Vulnerable backend: [`capstone/vulnerable_mobile_backend/app.py`](capstone/vulnerable_mobile_backend/app.py)
- Scenario guide: [`capstone/vulnerable_mobile_backend/README.md`](capstone/vulnerable_mobile_backend/README.md)
- Report template: [`capstone/audit_report_template.md`](capstone/audit_report_template.md)
- Training remediation patch: [`capstone/secure_remediation_patch/mobile_backend_secure.patch`](capstone/secure_remediation_patch/mobile_backend_secure.patch)

## Offline Learning Resources
- [`tools/debugger_cheatsheet.md`](tools/debugger_cheatsheet.md)
- [`tools/gdb_guide.md`](tools/gdb_guide.md)
- [`tools/radare2_guide.md`](tools/radare2_guide.md)
- [`tools/fuzzing_cheatsheet.md`](tools/fuzzing_cheatsheet.md)
- [`tools/memory_layout_reference.md`](tools/memory_layout_reference.md)
- [`tools/linux_security_flags.md`](tools/linux_security_flags.md)
- [`documentation/exploit_mitigation_theory.md`](documentation/exploit_mitigation_theory.md)
- [`documentation/aslr_dep_nx_explained.md`](documentation/aslr_dep_nx_explained.md)
- [`documentation/sandboxing_architecture.md`](documentation/sandboxing_architecture.md)

## GitHub Publishing Checklist
1. Confirm `README.md` renders correctly on GitHub (relative links should resolve).
2. Ensure `.gitignore` excludes `.venv`, build artifacts, `.pytest_cache`, and generated captures.
3. Run `source .venv/bin/activate && pytest -q tests` before pushing.
4. Optional: enable GitHub Actions to run `tests/` on push (workflow included).
5. Add a repository description and topics (e.g., `offensive-security`, `secure-coding`, `training-labs`).

## Safety Rules (Operational)
- Do not run against external networks or third-party services.
- Use local containers/VMs only.
- Prefer loopback interfaces (`127.0.0.1`) for packet and web labs.
- Review secure rewrite sections before extending any example.

## Legal Constraints (Enforced in This Repo)
- No real-world device jailbreaking instructions
- No commercial protection bypass guidance
- Labs run only in Linux VMs or Docker containers
- Vulnerabilities are intentionally created for training
- Secure remediation is included alongside exploit demonstration
