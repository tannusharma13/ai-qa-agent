RELEASE_PROMPT = """
You are a Senior QA Manager.

Analyze the following software testing results.

Execution Summary:
{summary}

Defect Details:
{defects}

Provide:

1. Coverage Assessment
2. Risk Assessment
3. Release Decision
   - READY FOR RELEASE
   - NOT READY FOR RELEASE

4. Reasons

5. Recommended Actions

Keep response professional and concise.
"""