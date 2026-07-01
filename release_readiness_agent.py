import os
import pandas as pd

from config.gemini import ask_ai
from release_prompt import RELEASE_PROMPT

# ---------------------------------
# Check Required Files
# ---------------------------------

execution_report = "output/execution_report.xlsx"
defect_report = "output/defect_report.xlsx"

if not os.path.exists(execution_report):
    raise FileNotFoundError(f"{execution_report} not found.")

if not os.path.exists(defect_report):
    raise FileNotFoundError(f"{defect_report} not found.")

# ---------------------------------
# Load Reports
# ---------------------------------

execution_df = pd.read_excel(execution_report)
defect_df = pd.read_excel(defect_report)

# ---------------------------------
# Calculate Test Summary
# ---------------------------------

total_tests = len(execution_df)

passed = len(
    execution_df[
        execution_df["status"] == "PASS"
    ]
)

failed = len(
    execution_df[
        execution_df["status"] == "FAIL"
    ]
)

pass_percentage = (
    (passed / total_tests) * 100
    if total_tests > 0
    else 0
)

summary = f"""
Total Tests : {total_tests}
Passed      : {passed}
Failed      : {failed}
Pass %      : {pass_percentage:.2f}%
"""

# ---------------------------------
# Prepare AI Prompt
# ---------------------------------

defects = defect_df.to_string(index=False)

prompt = RELEASE_PROMPT.format(
    summary=summary,
    defects=defects
)

print("📊 Generating Release Readiness Report...")

report = ask_ai(prompt)

# ---------------------------------
# Save Report
# ---------------------------------

os.makedirs("output", exist_ok=True)

output_file = "output/release_readiness_report.txt"

with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:
    file.write(report)

# ---------------------------------
# Display Report
# ---------------------------------

print("\n========== RELEASE READINESS ==========\n")
print(report)

print(f"\n✅ Release readiness report saved to {output_file}")