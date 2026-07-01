import os
import time
import pandas as pd

from config.gemini import ask_ai
from defect_prompt import DEFECT_TRIAGE_PROMPT

# ---------------------------------
# Load Execution Report
# ---------------------------------

execution_report = "output/execution_report.xlsx"

if not os.path.exists(execution_report):
    print("❌ execution_report.xlsx not found.")
    exit()

df = pd.read_excel(execution_report)

results = []

# ---------------------------------
# Analyze Failed Test Cases
# ---------------------------------

for _, row in df.iterrows():

    if row["status"] != "FAIL":
        continue

    print(f"\n🔍 Analyzing {row['test_id']}...")

    prompt = DEFECT_TRIAGE_PROMPT.format(
        expected=row["expected_result"],
        actual=row["actual_result"]
    )

    while True:
        try:
            analysis = ask_ai(prompt)
            break

        except Exception as e:
            print(f"⚠️ {e}")
            print("Retrying in 20 seconds...")
            time.sleep(20)

    results.append({
        "test_id": row["test_id"],
        "analysis": analysis
    })

    # Small delay to avoid hitting API limits
    time.sleep(2)

# ---------------------------------
# Save Report
# ---------------------------------

report_df = pd.DataFrame(results)

os.makedirs("output", exist_ok=True)

output_file = "output/defect_report.xlsx"

report_df.to_excel(
    output_file,
    index=False
)

print(f"\n✅ Defect triage completed.")
print(f"📄 Report saved to {output_file}")