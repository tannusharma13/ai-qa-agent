from config.gemini import ask_ai
from coverage_agent import COVERAGE_PROMPT
from prompts import TESTCASE_PROMPT

import pandas as pd
import json
import os
import sys


# Get Feature Description

if len(sys.argv) > 1:
    feature_description = sys.argv[1]
else:
    feature_description = input("Enter feature description:\n")

 
# Generate Test Cases

prompt = TESTCASE_PROMPT.format(
    feature=feature_description
)

print("Step 1: Generating Test Cases...")

result = ask_ai(prompt)

print("✅ Test Cases Generated")


# Coverage Analysis

coverage_prompt = COVERAGE_PROMPT.format(
    test_cases=result
)

print("Step 2: Generating Coverage Report...")

coverage_result = ask_ai(coverage_prompt)

print("✅ Coverage Report Generated")


# Display Results

print("\n========== GENERATED TEST CASES ==========\n")
print(result)

print("\n========== COVERAGE REPORT ==========\n")
print(coverage_result)


# Convert JSON Response to Excel

try:
    cleaned = (
        result
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    data = json.loads(cleaned)

    df = pd.DataFrame(data)

    os.makedirs("output", exist_ok=True)

    excel_path = "output/testcases.xlsx"

    df.to_excel(
        excel_path,
        index=False
    )

    print(f"\n✅ Excel file saved to {excel_path}")

except Exception as e:
    print("\n❌ Error while creating Excel file:")
    print(e)