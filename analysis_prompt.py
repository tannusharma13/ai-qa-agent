ANALYSIS_PROMPT = """
You are a QA Expert.

Compare the Expected Result and Actual Result.

Return JSON format:

{
    "status": "PASS or FAIL or PARTIAL PASS",
    "reason": "short explanation"
}

Expected Result:
{expected}

Actual Result:
{actual}
"""