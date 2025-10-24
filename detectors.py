import re

# Precompiled regex patterns (more precise)
SQL_PATTERNS = [
    # Real SQL injection patterns only
    re.compile(r"(?i)\bunion\s+select\b"),
    re.compile(r"(?i)\bdrop\s+table\b"),
    re.compile(r"(?i)\binsert\s+into\b"),
    re.compile(r"(?i)\bupdate\s+\w+\s+set\b"),
    re.compile(r"(?i)\bdelete\s+from\b"),
    re.compile(r"(?i)\bor\s+1\s*=\s*1\b"),
]

XSS_PATTERNS = [
    re.compile(r"(?i)<script.*?>.*?</script.*?>"),
    re.compile(r"(?i)on\w+\s*="),
    re.compile(r"(?i)javascript:"),
    re.compile(r"(?i)<img\s+src\s*=")
]

def detect_sql_injection(data: str) -> bool:
    """Detects SQL Injection patterns in the given data."""
    return any(p.search(data) for p in SQL_PATTERNS)

def detect_xss(data: str) -> bool:
    """Detects XSS attack patterns in the given data."""
    return any(p.search(data) for p in XSS_PATTERNS)

def detect_threat(data: str) -> str:
    """Returns the detected threat type, or an empty string if safe."""
    if detect_sql_injection(data):
        return "SQL Injection"
    elif detect_xss(data):
        return "XSS Attack"
    return ""
