import os
import pandas as pd

from config.gemini import ask_ai
from journey_prompt import JOURNEY_PROMPT

# ---------------------------------
# Check Execution Report
# ---------------------------------

execution_report = "output/execution_report.xlsx"

if not os.path.exists(execution_report):
    raise FileNotFoundError(f"{execution_report} not found.")

# ---------------------------------
# Load Execution Report
# ---------------------------------

df = pd.read_excel(execution_report)

failures = df[
    df["status"].str.upper() == "FAIL"
]

# ---------------------------------
# Handle No Failures
# ---------------------------------

if failures.empty:
    print("✅ No failed test cases found.")
    exit()

# ---------------------------------
# Build Failure Summary
# ---------------------------------

all_failures = ""

for _, row in failures.iterrows():

    all_failures += f"""
Test ID: {row['test_id']}

Scenario:
{row['scenario']}

Expected:
{row['expected_result']}

Actual:
{row['actual_result']}

---------------------------------------
"""

# ---------------------------------
# Generate Telecom Journey Analysis
# ---------------------------------

print("📱 Generating Telecom Journey Analysis...")

analysis = ask_ai(
    JOURNEY_PROMPT.format(
        failures=all_failures
    )
)

# ---------------------------------
# Save Report
# ---------------------------------

os.makedirs("output", exist_ok=True)

output_file = "output/telecom_journey_report.txt"

with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:
    file.write(analysis)

# ---------------------------------
# Display Report
# ---------------------------------

print("\n========== TELECOM JOURNEY ANALYSIS ==========\n")
print(analysis)

print(f"\n✅ Telecom Journey Analysis saved to {output_file}")