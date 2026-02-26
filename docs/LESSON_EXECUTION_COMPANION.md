# Lesson Execution Companion

Author: Simon Parris  
Date: 2026-02-26

Use this checklist to keep lab execution safe, repeatable, and professionally documented.

## Per-Lab Checklist

1. Confirm the lab is running locally (VM/container/loopback).
2. Read the safety scope and expected outcome.
3. Build/run the vulnerable example exactly as documented.
4. Record what happens before changing anything.
5. Inspect the code and identify the flaw class.
6. Review or implement the secure remediation.
7. Re-run verification commands/tests.
8. Write a short findings + remediation summary.

## Safety Prompts

- Is this action still confined to my local environment?
- Am I running the documented command, not improvising on a live target?
- Did I preserve the original output for comparison?

## Stop Conditions

Stop if:

- a command targets a non-local address/system
- you are unsure what a script modifies
- the lab leaves the documented local scope
