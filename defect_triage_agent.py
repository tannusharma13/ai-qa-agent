import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
from defect_prompt import DEFECT_TRIAGE_PROMPT
import os
import time

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

df = pd.read_excel(
    "output/execution_report.xlsx"
)

results = []

for index, row in df.iterrows():

    if row["status"] != "FAIL":
        continue

    expected = row["expected_result"]
    actual = row["actual_result"]

    print(f"\nAnalyzing {row['test_id']}...")

    while True:
        try:
            response = model.generate_content(
                DEFECT_TRIAGE_PROMPT.format(
                    expected=expected,
                    actual=actual
                )
            )
            break

        except Exception as e:
            print("Rate limit hit. Waiting 30 seconds...")
            time.sleep(30)

    results.append({
        "test_id": row["test_id"],
        "analysis": response.text
    })

    time.sleep(5)

    time.sleep(5)

report_df = pd.DataFrame(results)

report_df.to_excel(
    "output/defect_report.xlsx",
    index=False
)

print(
    "\nDefect Triage completed."
)