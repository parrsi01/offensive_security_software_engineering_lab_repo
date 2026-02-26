# Core Concepts

Author: Simon Parris  
Date: 2026-02-26

This repository teaches secure offensive security software engineering in a controlled, local-only training context with remediation built into the workflow.

## 1. Legal and Ethical Scope

- local systems, containers, and VMs only
- explicit authorization only
- no real-world targets
- remediation and safe practices included alongside demonstrations

## 2. Reproduce, Analyze, Remediate

Each lab should be approached as a software engineering workflow:

1. reproduce the vulnerable behavior safely
2. inspect the mechanism
3. document findings
4. apply a secure remediation
5. verify the fix

## 3. Mixed Skill Stack

- C memory safety fundamentals
- Python tooling/fuzzing/auditing
- basic web app security patterns
- Linux sandboxing concepts
- packet inspection and Dockerfile security review

## 4. Safety-by-Design

- labs are intentionally vulnerable for education
- examples are bounded and documented
- secure rewrite paths are part of the expected outcome
- tests validate both vulnerable and remediated behavior where practical
