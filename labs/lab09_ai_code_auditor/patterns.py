from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Pattern


@dataclass(frozen=True)
class InsecurePattern:
    id: str
    description: str
    regex: Pattern[str]
    severity: str
    secure_rewrite_hint: str


PATTERNS = [
    InsecurePattern(
        id="c_strcpy",
        description="Unbounded C string copy (strcpy)",
        regex=re.compile(r"\bstrcpy\s*\("),
        severity="high",
        secure_rewrite_hint="Use snprintf/strlcpy (if available) or a bounds-checked copy with length validation.",
    ),
    InsecurePattern(
        id="c_gets",
        description="Deprecated unsafe input function (gets)",
        regex=re.compile(r"\bgets\s*\("),
        severity="critical",
        secure_rewrite_hint="Use fgets with explicit buffer length and newline handling.",
    ),
    InsecurePattern(
        id="py_shell_true",
        description="subprocess execution with shell=True",
        regex=re.compile(r"subprocess\.(run|Popen|call)\([^\n]*shell\s*=\s*True"),
        severity="high",
        secure_rewrite_hint="Pass an argument list and keep shell=False unless documented and justified.",
    ),
    InsecurePattern(
        id="sql_string_concat",
        description="Possible SQL query concatenation",
        regex=re.compile(r"SELECT .*['\"]\s*\+\s*\w+", re.IGNORECASE),
        severity="medium",
        secure_rewrite_hint="Use parameterized queries with placeholders instead of concatenation.",
    ),
]
