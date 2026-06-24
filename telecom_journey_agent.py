import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
from journey_prompt import JOURNEY_PROMPT
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# STEP 3 - Read FAIL rows

df = pd.read_excel(
    "output/execution_report.xlsx"
)

failures = df[
    df["status"] == "FAIL"
]

# STEP 4 - Build failure summary

all_failures = ""

for _, row in failures.iterrows():

    all_failures += f"""
Test ID: {row['test_id']}
Scenario: {row['scenario']}
Expected: {row['expected_result']}
Actual: {row['actual_result']}

"""

response = model.generate_content(
    JOURNEY_PROMPT.format(
        failures=all_failures
    )
)

# STEP 5 - Save report

with open(
    "output/telecom_journey_report.txt",
    "w"
) as f:

    f.write(response.text)

print(response.text)
print("\nTelecom Journey Analysis Completed.")