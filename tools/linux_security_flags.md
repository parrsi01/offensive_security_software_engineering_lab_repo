# Linux Security Compile/Link Flags

## Useful Compiler Flags
- `-g -O0`: debug-friendly builds for labs
- `-Wall -Wextra -Werror`: stricter warning policy
- `-fstack-protector-strong`: stack canaries
- `-D_FORTIFY_SOURCE=2`: fortified libc checks (with optimization)
- `-fPIE -pie`: position-independent executable

## Useful Linker Flags
- `-Wl,-z,relro,-z,now`: RELRO + immediate binding
- `-Wl,-z,noexecstack`: non-executable stack

## Lab Comparison Mode
Training labs often compile both:
- unprotected binary (to observe unsafe behavior)
- protected binary (to observe mitigations and crash paths)
