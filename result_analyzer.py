from config.gemini import ask_ai
from analysis_prompt import ROOT_CAUSE_PROMPT

import pandas as pd
import os

# -------------------------------
# Load Execution Report
# -------------------------------
execution_report = "output/execution_report.xlsx"

if not os.path.exists(execution_report):
    raise FileNotFoundError(
        f"{execution_report} not found."
    )

df = pd.read_excel(execution_report)

# -------------------------------
# Collect Failed Test Cases
# -------------------------------
all_failures = ""

for _, row in df.iterrows():

    if row["status"].upper() == "FAIL":

        all_failures += f"""
Test ID: {row['test_id']}

Scenario:
{row['scenario']}

Expected:
{row['expected_result']}

Actual:
{row['actual_result']}

--------------------------------
"""

# -------------------------------
# Handle No Failures
# -------------------------------
if not all_failures.strip():

    print("✅ No failed test cases found.")
    exit()

# -------------------------------
# Generate Root Cause Analysis
# -------------------------------
print("Analyzing failures...")

analysis = ask_ai(
    ROOT_CAUSE_PROMPT.format(
        failures=all_failures
    )
)

# -------------------------------
# Display Analysis
# -------------------------------
print("\n========== ROOT CAUSE ANALYSIS ==========\n")
print(analysis)

# -------------------------------
# Save Report
# -------------------------------
os.makedirs("output", exist_ok=True)

report_path = "output/root_cause_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(analysis)

print(f"\n✅ Root cause report saved to {report_path}")