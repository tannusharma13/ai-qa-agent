import os
import google.generativeai as genai
from dotenv import load_dotenv
from approval_prompt import HITL_PROMPT

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

with open(
    "output/release_readiness_report.txt",
    "r"
) as f:

    release_report = f.read()

# STEP 4
response = model.generate_content(
    HITL_PROMPT.format(
        release_report=release_report
    )
)

print("\n===== AI RECOMMENDATION =====\n")
print(response.text)

# STEP 5
decision = input(
    "\nApprove Release? (yes/no): "
)

# STEP 6
with open(
    "output/final_release_decision.txt",
    "w"
) as f:

    f.write("AI Recommendation:\n\n")
    f.write(response.text)

    f.write("\n\nHuman Decision:\n")
    f.write(decision.upper())

print("\nFinal Decision Saved.")