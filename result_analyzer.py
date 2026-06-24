import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
from analysis_prompt import ROOT_CAUSE_PROMPT
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

df = pd.read_excel(
    "output/execution_report.xlsx"
)

all_failures = ""

for index, row in df.iterrows():

    if row["status"] == "FAIL":

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

print("Analyzing failures...")

response = model.generate_content(
    ROOT_CAUSE_PROMPT.format(
        failures=all_failures
    )
)

print("\nRoot Cause Analysis:\n")
print(response.text)

with open(
    "output/root_cause_report.txt",
    "w"
) as f:

    f.write(response.text)

print(
    "\nRoot cause report saved to output/root_cause_report.txt"
)