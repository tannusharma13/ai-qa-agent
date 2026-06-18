from coverage_agent import COVERAGE_PROMPT
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import TESTCASE_PROMPT
import pandas as pd
import json
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

feature = input(
    "Enter feature description:\n"
)

prompt = TESTCASE_PROMPT.format(
    feature=feature
)
print("Step 1: Generating test cases...")

response = model.generate_content(prompt)

print("Step 2: Test cases generated!")

result = response.text

print("Step 3: Generating coverage report...")

coverage_prompt = COVERAGE_PROMPT.format(
    test_cases=result
)

coverage_response = model.generate_content(
    coverage_prompt
)

print("Step 4: Coverage report generated!")


print("\nGenerated Test Cases:\n")
print(result)

print("\nCoverage Report:\n")
print(coverage_response.text)

# Remove markdown wrappers
cleaned = (
    result
    .replace("```json", "")
    .replace("```", "")
    .strip()
)

# Convert JSON string to Python object
data = json.loads(cleaned)

# Convert to DataFrame
df = pd.DataFrame(data)

# Export Excel
df.to_excel(
    "output/testcases.xlsx",
    index=False
)

print("\nExcel file saved to output/testcases.xlsx")