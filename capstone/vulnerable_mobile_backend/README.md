# Capstone: Vulnerable Mock Mobile Backend

Author: Simon Parris  
Generated: 2026-02-24

## Scenario
A mock mobile backend exposes a `/session` endpoint backed by SQLite. The vulnerable mode concatenates `user_id` directly into SQL. Learners must document risk, demonstrate the issue locally, and apply the included remediation patch.

## Safe Scope
- Local Flask service only (`127.0.0.1`)
- Intentionally vulnerable training code
- No commercial app protection bypassing

## Run Instructions
```bash
cd capstone/vulnerable_mobile_backend
PYTHONPATH=../.. python3 app.py
```

## Assessment Deliverables
- Technical vulnerability report (use template)
- Risk assessment and business impact summary
- Remediation patch validation
- Secure architecture redesign notes
