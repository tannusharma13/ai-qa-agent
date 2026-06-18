TESTCASE_PROMPT = """
You are a Senior Telecom QA Engineer.

Generate test cases for the feature.

For each test case provide:

- test_id
- type
- priority
- scenario
- expected_result

Return ONLY valid JSON array.

Feature:
{feature}
"""