# Privilege Escalation Theory (Defensive Understanding)

Author: Simon Parris  
Generated: 2026-02-24

## Scope Note
This document explains concepts for defensive understanding only. The labs in this repository do not provide real-world privilege escalation instructions.

## Concepts
- Vertical escalation: increasing privileges on the same host.
- Horizontal escalation: accessing another user/account with equal privilege level.
- Common root causes: weak access control, unsafe defaults, excessive privileges, insecure service boundaries.

## Defensive Controls
- Least privilege by default
- Strong authorization checks server-side
- Isolation boundaries (namespaces/containers/VMs)
- Auditing and monitoring for privilege changes
