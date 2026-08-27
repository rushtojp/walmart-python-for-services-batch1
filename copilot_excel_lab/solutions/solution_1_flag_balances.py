# Solution 1 — Read leave_balances.xlsx and flag risky balances
# Matches Prompts 1-3 in COPILOT_PROMPTS.md
# Expected: exactly 3 flagged rows (E1018 negative, E1019 zero, E1020 low)

import pandas as pd

df = pd.read_excel("../data/leave_balances.xlsx", sheet_name="LeaveBalances", nrows=20)

def flag(balance):
    if balance < 0:
        return "NEGATIVE - investigate"
    elif balance == 0:
        return "ZERO - no leave left"
    elif balance < 3:
        return "LOW - below 3 days"
    return "OK"

df["Flag"] = df["Balance"].apply(flag)

flagged = df[df["Flag"] != "OK"]
print("Flagged employees:")
print(flagged[["EmployeeID", "Name", "Department", "Balance", "Flag"]].to_string(index=False))
print(f"\nTotal flagged: {len(flagged)} (expected: 3)")

# Verification check — the 'done means' test
expected = {"E1018", "E1019", "E1020"}
actual = set(flagged["EmployeeID"])
assert actual == expected, f"MISMATCH: got {actual}"
print("PASS: all 3 planted cases flagged correctly")
