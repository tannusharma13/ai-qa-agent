import os

print("===== QA COPILOT STARTED =====")

print("\nRunning Test Generation...")
os.system("python3 app.py")

print("\nRunning Coverage Analysis...")
os.system("python3 coverage_agent.py")

print("\nRunning Execution Agent...")
os.system("python3 execution_agent.py")

print("\nRunning Root Cause Analysis...")
os.system("python3 result_analyzer.py")

print("\nRunning Defect Triage...")
os.system("python3 defect_triage_agent.py")

print("\nRunning Release Readiness...")
os.system("python3 release_readiness_agent.py")

print("\nRunning Human Approval...")
os.system("python3 hitl_agent.py")

print("\n===== QA PIPELINE COMPLETED =====")