# Capstone Secure Remediation Patch

Author: Simon Parris  
Generated: 2026-02-24

## Contents
- `mobile_backend_secure.patch`: parameterized query remediation for the mock mobile backend SQL injection simulation.

## Patch Application (Training)
```bash
cd capstone/vulnerable_mobile_backend
patch -p0 < ../secure_remediation_patch/mobile_backend_secure.patch
```

## Validation
- Start the backend locally.
- Re-run the reproduction request from the report.
- Confirm injected input no longer returns unauthorized rows.
