import os

from config.gemini import ask_ai
from approval_prompt import HITL_PROMPT

# ---------------------------------
# Check Release Report
# ---------------------------------

report_file = "output/release_readiness_report.txt"

if not os.path.exists(report_file):
    raise FileNotFoundError(f"{report_file} not found.")

with open(
    report_file,
    "r",
    encoding="utf-8"
) as file:
    release_report = file.read()

# ---------------------------------
# AI Recommendation
# ---------------------------------

print("🤖 Generating AI Recommendation...")

recommendation = ask_ai(
    HITL_PROMPT.format(
        release_report=release_report
    )
)

print("\n========== AI RECOMMENDATION ==========\n")
print(recommendation)

# ---------------------------------
# Human Approval
# ---------------------------------

while True:

    decision = input(
        "\nApprove Release? (yes/no): "
    ).strip().lower()

    if decision in ["yes", "no"]:
        break

    print("❌ Please enter only 'yes' or 'no'.")

final_decision = (
    "APPROVED"
    if decision == "yes"
    else "REJECTED"
)

# ---------------------------------
# Save Decision
# ---------------------------------

os.makedirs("output", exist_ok=True)

output_file = "output/final_release_decision.txt"

with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    file.write("========== AI QA COPILOT ==========\n\n")

    file.write("AI Recommendation\n")
    file.write("-----------------\n")
    file.write(recommendation)

    file.write("\n\n")

    file.write("Human Decision\n")
    file.write("-----------------\n")
    file.write(final_decision)

print(f"\n✅ Final decision saved to {output_file}")