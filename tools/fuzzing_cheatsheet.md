# Fuzzing Cheatsheet

## Core Terms
- Corpus: initial sample inputs used to start fuzzing
- Mutation: randomized changes applied to existing inputs
- Crash: abnormal termination or exception caused by an input
- Triage: classifying crashes by root cause and reproducibility

## Minimal Loop
1. Select or generate input
2. Execute target
3. Detect crash/timeout
4. Save reproducer
5. Repeat and report

## Training Safety
- Fuzz only intentionally vulnerable local targets
- Set iteration/time limits
- Log exact crashing input for remediation testing
