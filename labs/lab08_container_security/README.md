# Lab08: Container Security (Misconfiguration and Hardening)

Author: Simon Parris  
Generated: 2026-02-24

## Concept Overview
This lab compares a vulnerable and hardened Dockerfile. The vulnerable version runs as root and includes development-mode settings; the hardened version uses a non-root user and safer defaults.

## Threat Model
- Asset: container runtime isolation and application filesystem integrity
- Attacker capability: code execution inside a containerized app process
- Unsafe condition: root user, broad file copies, insecure runtime configuration
- Impact: privilege abuse inside container, increased breakout risk, secrets exposure
- Training scope: local Docker builds only

## Step-by-Step CLI Instructions
```bash
cd labs/lab08_container_security
python3 scan_dockerfile.py
bash build_examples.sh
```

## VS Code Workflow Instructions
1. Diff `Dockerfile.vulnerable` vs `Dockerfile.hardened`.
2. Run the scanner script in the terminal.
3. If Docker is installed, build both images using the printed commands.

## Expected Output
- Scanner flags root runtime and development mode in the vulnerable Dockerfile.
- Hardened Dockerfile produces fewer/no findings under the simple rule set.

## Common Debugging Errors
- `docker: command not found`: install Docker for full execution.
- Permission denied to Docker socket: add user to Docker group or use sudo in a VM.
- Scanner false positives/negatives: simple rule-based scanner is intentionally limited.

## Secure Rewrite
Implemented hardening patterns:
- non-root execution user
- explicit ownership of app directory
- safer environment defaults
- review of broad `COPY` behavior (further improved with `.dockerignore` in production)

## Security Implications
Container hardening reduces blast radius but does not replace secure application code, runtime policies, and image provenance controls.

## Professional Skill Alignment
- DevSecOps / Security Software Engineer: container baseline hardening
- Application Security Engineer: deployment misconfiguration review
