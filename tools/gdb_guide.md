# GDB Guide (Offline Lab Workflow)

## Compile for Analysis
```bash
gcc -O0 -g -fno-stack-protector -no-pie demo.c -o demo
```

## Suggested Workflow
1. Start with `gdb ./demo`.
2. Set `break main` and `run`.
3. Disassemble the active function with `disassemble`.
4. Inspect stack/registers before and after input handling.
5. Record observations in a notes file (offsets, changed values, branch behavior).

## Common Mistakes
- Compiling without `-g` (reduced source-level visibility)
- Optimized builds (variable locations appear inconsistent)
- Forgetting arguments for input-dependent code paths
