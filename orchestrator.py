import subprocess
import sys

from config.logger import logger

print("=" * 50)
print("AI QA COPILOT")
print("=" * 50)

logger.info("AI QA Copilot Started")

feature = input("\nEnter Feature Description:\n")


def run_step(title, command):
    """
    Runs one pipeline step.
    Stops the entire pipeline if the step fails.
    """

    logger.info(title)

    result = subprocess.run(command)

    if result.returncode != 0:

        logger.error(f"{title} FAILED")
        logger.error("Pipeline Stopped")
        logger.error("Remaining agents were NOT executed.")

        print("\n" + "=" * 50)
        print("PIPELINE STOPPED")
        print("=" * 50)

        sys.exit(result.returncode)

    logger.info(f"{title} COMPLETED")


# ----------------------------------
# Phase 1
# ----------------------------------

run_step(
    "Running Test Case Generation...",
    ["python3", "app.py", feature]
)

# ----------------------------------
# Phase 2
# ----------------------------------

run_step(
    "Running Execution Agent...",
    ["python3", "execution_agent.py"]
)

# ----------------------------------
# Phase 3
# ----------------------------------

run_step(
    "Running Root Cause Analysis...",
    ["python3", "result_analyzer.py"]
)

# ----------------------------------
# Phase 4
# ----------------------------------

run_step(
    "Running Defect Triage...",
    ["python3", "defect_triage_agent.py"]
)

# ----------------------------------
# Phase 5
# ----------------------------------

run_step(
    "Running Release Readiness...",
    ["python3", "release_readiness_agent.py"]
)

# ----------------------------------
# Phase 6
# ----------------------------------

run_step(
    "Running Human Approval...",
    ["python3", "hitl_agent.py"]
)

# ----------------------------------
# Phase 7
# ----------------------------------

run_step(
    "Running Telecom Journey Validation...",
    ["python3", "telecom_journey_agent.py"]
)

logger.info("QA Pipeline Completed Successfully")

print("\n" + "=" * 50)
print("QA PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 50)