# Repository Status Report

Author: Simon Parris  
Date: 2026-02-26

## Scope

Safe, local-only offensive security software engineering curriculum with reproducible labs, documentation, tests, and capstone deliverables.

## Implemented Areas

- legal/ethical scope in root README
- course overview and roadmap
- nine hands-on labs spanning memory safety, sandboxing, fuzzing, web security, packet analysis, container security, and AI code auditing
- tests for selected labs and remediations
- theory/documentation and debugger/tool references
- capstone mock mobile backend audit scenario
- CI workflow

## Repository Quality Upgrades (2026-02-26)

- added `LICENSE` (MIT)
- added `Makefile`, `pyproject.toml`, and `requirements.in`
- added `docs/` core manuals and portfolio docs
- added `validate_repo.sh` for structure/syntax/readiness validation

## Readiness Notes

- Full lab execution may require Ubuntu tooling, GCC, Docker, and optional debuggers.
- Validator avoids executing potentially environment-dependent lab payloads by default.
