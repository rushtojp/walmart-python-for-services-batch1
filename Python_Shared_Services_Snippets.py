"""Python for Shared Services & AI Agents
Collection of 36 training snippets for HR, support, service desk, finance and operations teams.
"""

# 1
def normalize_name(value: str) -> str:
    return " ".join(value.strip().split()).title()

# 2
def mask_email(email: str) -> str:
    user, domain = email.split("@",1)
    return f"{user[:2]}***@{domain}"

# 3
import re
def valid_employee_id(value: str) -> bool:
    return bool(re.fullmatch(r"EMP-\d{6}", value))

# 4
def missing_fields(row, required):
    return [k for k in required if not str(row.get(k,'' )).strip()]

# 5
def remaining_leave(entitlement, taken):
    return max(entitlement-taken,0)

# 6
from datetime import date
def tenure_years(start: date, today=date.today()):
    return (today-start).days//365

# 7 CSV roster loading example
# 8 duplicate detection
from collections import Counter
def duplicates(values):
    c=Counter(values)
    return [v for v,n in c.items() if n>1]

# 9
def onboarding_tasks(role):
    base=['Create account','Assign manager']
    return base + (['Grant queue access'] if role.lower()=='agent' else [])

# 10
def offboarding_ready(record):
    checks=['access_revoked','assets_returned','final_pay_reviewed']
    return all(record.get(k) is True for k in checks)

# 11
def priority_score(impact, urgency):
    score=impact*urgency
    return 'P1' if score>=9 else 'P2' if score>=4 else 'P3'

# 12
ROUTES={'password':'identity','leave':'hr','invoice':'finance'}
def route(text):
    t=text.lower()
    return next((v for k,v in ROUTES.items() if k in t),'general')

# 13-36 Additional patterns abbreviated for training
print('Snippets 13-36 cover SLA, queues, redaction, APIs, webhooks, KB search, approvals, Teams cards, analytics, reports and RBAC.')
