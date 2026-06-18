EXECUTION_ANALYSIS_PROMPT = """
You are a Senior QA Engineer.

Expected Result:
{expected}

Actual Result:
{actual}

Compare both.

Return JSON:

{
    "status":"PASS or FAIL",
    "reason":"short explanation"
}
"""