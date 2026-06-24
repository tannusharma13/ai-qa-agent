ROOT_CAUSE_PROMPT = """
You are a Senior QA Engineer.

Analyze the failed test case.

Expected Result:
{expected}

Actual Result:
{actual}

Provide:

1. Root Cause
2. Severity
3. Impacted Module
4. Recommendation
"""