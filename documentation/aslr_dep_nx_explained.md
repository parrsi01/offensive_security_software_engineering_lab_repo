# ASLR / DEP / NX Explained

Author: Simon Parris  
Generated: 2026-02-24

## ASLR
Address Space Layout Randomization changes memory locations between runs, making hard-coded addresses unreliable.

## DEP / NX
Data Execution Prevention (NX bit) marks stack/heap pages as non-executable, reducing straightforward payload execution from data regions.

## Training Relevance
Lab01 compares compiled binaries with and without common hardening flags so learners can observe the differences in runtime behavior and debugging workflows.
