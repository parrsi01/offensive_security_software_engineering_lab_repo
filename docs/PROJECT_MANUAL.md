# Project Manual

Author: Simon Parris  
Date: 2026-02-26

## Purpose

This repository provides a safe, reproducible environment for learning vulnerability analysis, exploit engineering fundamentals, and secure remediation as software engineering practice.

## Operating Rules (Mandatory)

- Use local VMs/containers only.
- Do not target external systems.
- Follow the repo ethical disclaimer and legal constraints.
- Prefer the documented scripts and workflows over improvisation.

## Standard Lab Workflow

1. Read the lab `README.md`
2. Review safety notes and prerequisites
3. Build/run the local demonstration
4. Record the vulnerable behavior and evidence
5. Study the mechanism and mitigation
6. Apply or review the secure rewrite
7. Run verification/tests where provided
8. Document what changed and why

## Evidence Standard

- reproduction steps
- observed vulnerable behavior
- code path / root cause notes
- mitigation summary
- verification output

## Quality Gates Before Push

1. `./validate_repo.sh --quick`
2. `make lint`
3. `pytest -q tests` (when dependencies are installed)
