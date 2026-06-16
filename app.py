import google.generativeai as genai
from prompts import TESTCASE_PROMPT
import pandas as pd
import json

API_KEY = "YOUR_API_KEY"

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

response = model.generate_content(
    prompt
)

result = response.text

print("\nGenerated Test Cases:\n")
print(result)

# Remove markdown if Gemini returns it

cleaned = result.replace(
    "```json",
    ""
).replace(
    "```",
    ""
)

data = json.loads(cleaned)

df = pd.DataFrame(data)

df.to_excel(
    "output/testcases.xlsx",
    index=False
)

print(
    "\nExcel file created: output/testcases.xlsx"
)