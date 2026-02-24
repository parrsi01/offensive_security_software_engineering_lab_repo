# Lab03: Linux Sandbox Simulation (Namespace Misconfiguration and Hardening)

Author: Simon Parris  
Generated: 2026-02-24

## Concept Overview
This lab compares partial namespace isolation (misconfigured sandbox) with a more complete namespace-based isolation attempt. The goal is to understand why “some isolation” is not equivalent to a secure sandbox.

## Threat Model
- Asset: host filesystem, process visibility, network namespace boundaries
- Attacker capability: code execution inside a local training process
- Unsafe condition: incomplete namespace isolation (e.g., no mount/net isolation)
- Impact: sandbox escape opportunities, host data exposure, false assurance
- Training scope: local Linux VM only; no privilege escalation content

## Step-by-Step CLI Instructions
```bash
cd labs/lab03_linux_sandbox_simulation
bash verify_isolation.sh
bash sandbox_demo.sh
bash sandbox_hardened.sh
```

## VS Code Workflow Instructions
1. Open the three scripts in tabs.
2. Run `verify_isolation.sh` first to capture host namespace IDs.
3. Run `sandbox_demo.sh` and compare IDs.
4. Run `sandbox_hardened.sh` and compare again.
5. Note which namespaces changed and which remained shared.

## Expected Output
- Host namespace IDs printed.
- Misconfigured demo prints a warning that network/filesystem isolation is incomplete.
- Hardened demo either shows additional namespace separation or reports kernel restrictions.

## Common Debugging Errors
- `unshare not installed`: install `util-linux`.
- `Operation not permitted`: user namespaces or network namespaces disabled by host policy.
- Missing namespace output in a container: restricted `/proc` visibility.

## Secure Rewrite
Use layered isolation rather than a single namespace flag:
- user + mount + pid + net namespaces
- minimal filesystem view
- read-only mounts where possible
- drop capabilities and seccomp in containerized deployments

## Security Implications
Sandboxing failures are often configuration failures, not code bugs. Engineers must verify the isolation properties actually enforced at runtime.

## Professional Skill Alignment
- Security Software Engineer: sandbox design and validation
- Offensive Security Engineer (Legal Context): identify misconfigurations in a local test environment
- Application Security Engineer: document isolation assumptions and controls
