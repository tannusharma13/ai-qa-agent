ROOT_CAUSE_PROMPT = """
You are a Senior QA Engineer.

Analyze the failed test cases below.

For each failure provide:

1. Root Cause
2. Severity (Low/Medium/High/Critical)
3. Suggested Fix

Failures:

{failures}
"""