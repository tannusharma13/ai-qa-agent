DEFECT_TRIAGE_PROMPT = """
You are a Senior QA Manager.

Analyze the defect.

Expected Result:
{expected}

Actual Result:
{actual}

Provide:

1. Defect Category
2. Severity
3. Priority
4. Suggested Owner Team
5. Explanation
"""