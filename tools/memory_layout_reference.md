# Memory Layout Reference (Linux Process)

Typical high-level regions:
- Text/code segment: executable instructions
- Data segment: initialized globals/statics
- BSS: zero-initialized globals/statics
- Heap: dynamic allocations (`malloc`)
- Stack: function frames, local variables, return addresses

Notes:
- Actual addresses vary with ASLR.
- NX/DEP marks selected regions non-executable.
- Stack canaries detect some overwrite attempts before function return.
