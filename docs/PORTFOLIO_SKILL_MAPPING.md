# Portfolio Skill Mapping

Author: Simon Parris  
Date: 2026-02-26

This document maps repo components to professional skills for security software engineering, appsec, and controlled vulnerability research roles.

## Memory Safety & Native Code Analysis

Mapped components:

- `labs/lab01_stack_overflow/`
- `labs/lab02_memory_corruption_suite/`
- `tests/test_lab01.py`

Skills demonstrated:

- secure C coding awareness
- memory corruption class identification
- build/test verification for vulnerable vs remediated behavior

## Sandboxing / OS Security Concepts

Mapped components:

- `labs/lab03_linux_sandbox_simulation/`
- `documentation/sandboxing_architecture.md`

Skills demonstrated:

- Linux isolation/sandboxing concepts
- secure configuration reasoning
- verification mindset for containment claims

## Security Tooling & Analysis Automation

Mapped components:

- `labs/lab04_simple_fuzzer_engine/`
- `labs/lab09_ai_code_auditor/`
- `tests/test_lab04_fuzzer.py`
- `tests/test_lab09_ai_auditor.py`

Skills demonstrated:

- Python security tooling implementation
- fuzzing basics and crash logging
- static pattern auditing and secure rewrite hints
- unit-test-backed tooling validation

## Web / Network / Container Security

Mapped components:

- `labs/lab06_mock_web_vulnerability/`
- `labs/lab07_packet_analysis/`
- `labs/lab08_container_security/`
- `tests/test_web_app_security.py`

Skills demonstrated:

- insecure input handling vs secure parameterization
- packet/header inspection fundamentals
- Dockerfile hardening analysis
- test-driven validation of security behavior

## Capstone / Professional Reporting

Mapped components:

- `capstone/`
- `COURSE_OVERVIEW.md`
- `ROADMAP.md`

Skills demonstrated:

- audit scenario execution
- remediation patch review
- security findings documentation
- structured learning progression and deliverable management

## CV-Ready Bullet Statements

- Built a controlled offensive security software engineering lab with nine local-only labs, tests, and capstone deliverables covering vulnerability analysis and secure remediation.
- Implemented and validated Python-based security tooling (fuzzer and code auditor) with unit tests and documentation-first workflows.
- Practiced secure web, container, packet, and native code analysis in sandboxed environments with explicit legal/ethical constraints and reproducible verification steps.
