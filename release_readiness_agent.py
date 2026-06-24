import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
from release_prompt import RELEASE_PROMPT
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

execution_df = pd.read_excel(
    "output/execution_report.xlsx"
)

defect_df = pd.read_excel(
    "output/defect_report.xlsx"
)

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

summary = f"""
Total Tests: {total_tests}
Passed: {passed}
Failed: {failed}
Pass Percentage: {(passed/total_tests)*100:.2f}%
"""

defects = defect_df.to_string()

response = model.generate_content(
    RELEASE_PROMPT.format(
        summary=summary,
        defects=defects
    )
)

report = response.text

with open(
    "output/release_readiness_report.txt",
    "w"
) as file:
    file.write(report)

print(report)

print(
    "\nRelease readiness report generated."
)