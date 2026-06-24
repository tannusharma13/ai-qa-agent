JOURNEY_PROMPT = """
You are a Telecom QA Risk Analyst.

Analyze the failed telecom test cases below:

{failures}

Provide:

1. Affected Customer Journey
2. Business Impact
3. Risk Level (Low/Medium/High)
4. Recommendations

Keep response concise.
"""