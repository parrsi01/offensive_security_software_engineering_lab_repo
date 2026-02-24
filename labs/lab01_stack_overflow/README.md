# Lab01: Stack Overflow (Intentional Stack Overwrite Simulation)

Author: Simon Parris  
Generated: 2026-02-24

## Concept Overview
This lab demonstrates a stack-based buffer overflow pattern in a safe training design. Instead of teaching control-flow hijacking, the program uses a local struct with a buffer and adjacent guard value. When input is too long, the guard changes, proving adjacent stack data was overwritten.

## Threat Model
- Asset: application memory integrity and control-flow safety
- Attacker capability: local user can provide untrusted CLI input
- Unsafe condition: unbounded copy into fixed-size stack buffer
- Impact (real systems): memory corruption, crashes, code execution, data corruption
- Training scope: local VM/container only; intentionally vulnerable sample binary

## Step-by-Step CLI Instructions
```bash
cd labs/lab01_stack_overflow
bash build.sh
./build/vuln_unprotected SAFE
./build/vuln_unprotected AAAAAAAAAAAAAAAAAAAAAAAA || true
./build/secure_fixed AAAAAAAAAAAAAAAAAAAAAAAA || true
```

### Compile Protected vs Unprotected
- `build/vuln_unprotected`: compiled with mitigations intentionally reduced for observation
- `build/vuln_protected`: compiled with stack protector, PIE, RELRO, NX stack
- `build/secure_fixed`: bounded-copy secure rewrite

## VS Code Workflow Instructions
1. Open the repository in VS Code.
2. Open terminal: `Terminal -> New Terminal`.
3. Run `bash labs/lab01_stack_overflow/build.sh`.
4. Open `labs/lab01_stack_overflow/src/vulnerable_stack_overflow.c` side-by-side with terminal.
5. Run the binaries and compare `guard` values.
6. Optionally launch GDB using the commands below.

## GDB Workflow (Recommended)
```bash
cd labs/lab01_stack_overflow
gdb ./build/vuln_unprotected
(gdb) break handle_input
(gdb) run AAAAAAAAAAAAAAAAAAAAAAAA
(gdb) next
(gdb) info locals
(gdb) x/32xb &frame
```

## Expected Output
Safe input on vulnerable binary:
```text
buffer=SAFE
guard=0xb16b00b5
No overflow observed for this input length.
```

Oversized input on vulnerable binary:
```text
buffer=AAAAAAAA...
guard=0x41414141
OVERFLOW_SIMULATED: adjacent stack data was modified.
```

Secure binary with oversized input:
```text
Rejected input: length 24 exceeds safe buffer size 15.
```

## Common Debugging Errors
- `No such file or directory`: build step not run yet.
- `gcc: command not found`: install build tools (`build-essential`).
- Different `guard` value than expected: compiler optimization flags changed; use `-O0` as provided.
- GDB shows optimized-out variables: ensure debug binary built with `-g -O0`.

## Secure Rewrite
The secure version applies two controls:
- length validation before copy
- bounded write with explicit destination size (`snprintf`)

Additional production recommendations:
- centralize input validation
- return structured error codes
- add unit tests for boundary lengths

## Security Implications
This pattern maps to real memory-safety classes that are often high severity. Even when code execution is not demonstrated, silent memory corruption can invalidate security assumptions, audit logs, and program correctness.

## Professional Skill Alignment
- Junior Vulnerability Researcher: identify unsafe memory copies and reproduce corruption
- Security Software Engineer: implement safe bounds checks and compile hardening flags
- Reverse Engineering Analyst: inspect stack state in GDB
- Application Security Engineer: document root cause and remediation
