# Lab02: Memory Corruption Suite (Format String, Integer Overflow, UAF Simulation)

Author: Simon Parris  
Generated: 2026-02-24

## Concept Overview
This lab bundles three intentionally insecure patterns that commonly appear in vulnerability research triage:
- format string misuse (`printf(user_input)`)
- integer overflow in size calculations
- use-after-free lifecycle mistakes (demonstrated safely as a simulation)

Each vulnerable example is paired with secure coding guidance and a secure rewrite binary.

## Threat Model
- Asset: memory integrity, data correctness, and process stability
- Attacker capability: can supply malformed CLI input values
- Unsafe conditions: unsanitized format strings, unchecked arithmetic, pointer lifecycle misuse
- Impact (real systems): memory disclosure, corruption, crashes, logic bypass, unexpected allocations
- Training scope: local binaries only; no persistence or privilege escalation content

## Step-by-Step CLI Instructions
```bash
cd labs/lab02_memory_corruption_suite
bash build_all.sh
./build/format_string_demo "%x %x %x"
./build/integer_overflow_demo 64 || true
./build/use_after_free_simulation
./build/secure_rewrites "hello" 10
```

## VS Code Workflow Instructions
1. Open `labs/lab02_memory_corruption_suite/src/` files in separate tabs.
2. Build with `bash labs/lab02_memory_corruption_suite/build_all.sh`.
3. Run each binary from the terminal and compare vulnerable vs secure behavior.
4. Add breakpoints in GDB for `main` and inspect variable values after parsing user input.

## Expected Output
Format string demo prints user-controlled formatted output (unsafe).

Integer overflow demo with `64` shows wrap-around in a 16-bit total size:
```text
requested=64 bytes_per_record=1024 total_size=0
INTEGER_OVERFLOW_SIMULATED: total_size wrapped around.
```

Use-after-free simulation prints lifecycle warnings and secure pointer clearing guidance.

## Common Debugging Errors
- Shell expands `%` unexpectedly when quoted incorrectly: wrap format strings in quotes.
- Integer overflow demo output differs: use the provided compiler and `-O0` build path.
- Warning about non-literal format string: expected for the vulnerable training sample.

## Secure Rewrite
The secure rewrite binary demonstrates:
- explicit format strings (`printf("%s", user_input)` pattern)
- checked multiplication before allocation sizing
- strict numeric parsing with `strtoul` validation
- pointer invalidation (`ptr = NULL`) after free

## Security Implications
These issues frequently appear during source review and reverse engineering. They can expose memory, corrupt state, or cause logic errors that impact security decisions.

## Professional Skill Alignment
- Junior Vulnerability Researcher: recognize memory corruption patterns during triage
- Security Software Engineer: implement arithmetic safety and pointer lifecycle hygiene
- Reverse Engineering Analyst: map unsafe code paths to runtime state
- Application Security Engineer: prioritize fixes and write remediation guidance
