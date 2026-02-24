# Sandboxing Architecture

Author: Simon Parris  
Generated: 2026-02-24

## Layered Model
- VM boundary (strong isolation for training labs)
- Container runtime controls (namespaces, cgroups, seccomp, capabilities)
- Process-level sandboxing (chroot/jail-like patterns, language runtime sandboxes)
- Application-level authorization and validation

## Common Failure Modes
- Partial isolation mistaken for full isolation
- Excessive privileges/capabilities
- Shared writable mounts with sensitive data
- Missing runtime policy enforcement

## Lab Link
Lab03 demonstrates the gap between partial namespace usage and a more hardened namespace configuration attempt.
