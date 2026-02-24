# Debugger Cheatsheet (GDB Focus)

- Start binary: `gdb ./binary`
- Run with args: `run AAAA`
- Breakpoint at function: `break main`
- Breakpoint at source line: `break file.c:42`
- Continue: `continue`
- Step into: `step`
- Step over: `next`
- Inspect registers: `info registers`
- Backtrace: `bt`
- Inspect stack bytes: `x/32xb $rsp`
- Inspect string at pointer: `x/s <addr>`
- Disassemble function: `disassemble main`
- Show locals: `info locals`
- Quit: `quit`

Tip: Compile with `-g -O0` for deterministic stepping in training labs.
