# Solution 2 — Ticket counts by queue, monthly pivot, export to Excel
# Matches Prompts 4-6 in COPILOT_PROMPTS.md
# Verification: pivot grand total must equal the raw row count (60)

import pandas as pd

df = pd.read_csv("../data/tickets.csv", parse_dates=["DateOpened"])

# 1. Counts per queue, sorted descending
counts = df["Queue"].value_counts()
print("Tickets per queue:")
print(counts.to_string())

# 2. Monthly pivot: rows = month, columns = queue
df["Month"] = df["DateOpened"].dt.to_period("M").astype(str)
pivot = pd.pivot_table(df, index="Month", columns="Queue",
                       values="TicketID", aggfunc="count", fill_value=0)
print("\nMonthly pivot:")
print(pivot)

# 3. Verification — pivot total reconciles to raw file
assert pivot.values.sum() == len(df), "Pivot total does not match raw row count"
print(f"\nPASS: pivot total ({pivot.values.sum()}) == raw rows ({len(df)})")

# 4. Export to Excel with two sheets
with pd.ExcelWriter("../data/ticket_summary_output.xlsx", engine="openpyxl") as xw:
    counts.rename("Count").to_excel(xw, sheet_name="ByQueue")
    pivot.to_excel(xw, sheet_name="MonthlyPivot")
print("Written: ticket_summary_output.xlsx")
