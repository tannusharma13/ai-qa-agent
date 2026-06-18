import pandas as pd

df = pd.read_excel(
    "output/testcases.xlsx"
)
actual_results = []

statuses = []
sample_actual_results = [
    "Roaming pack activated successfully.",
    "Insufficient balance message displayed.",
    "Credit limit exceeded message displayed.",
    "Pack already active message displayed.",
    "No Internet Connection displayed.",
    "Pack list loaded successfully.",
    "Country filter worked correctly.",
    "SMS not received after activation.",
    "Active pack visible in account.",
    "Multi-country pack activated successfully.",
    "HTTP 500 Internal Server Error.",
    "Back navigation working correctly.",
    "Eligibility validation displayed.",
    "Promotional pack activated successfully.",
    "Pack list loaded in 12 seconds.",
    "User redirected to login page.",
    "Conflict validation displayed.",
    "Prompt shown to enable roaming service.",
    "Pack activated while abroad.",
    "UI broken on iPhone SE screen."
]

for index, row in df.iterrows():

    print("\n-------------------")

    print("Test ID:", row["test_id"])

    print("Scenario:")
    print(row["scenario"])

    print("\nExpected:")
    print(row["expected_result"])

   
    
    actual_result = sample_actual_results[index]
    actual_results.append(actual_result)

    if index in [7, 10, 14, 19]:

        statuses.append("FAIL")

    else:

        statuses.append("PASS")

    print("\nActual:")
    print(actual_result)
    



df["actual_result"] = actual_results
df["status"] = statuses

df.to_excel(
    "output/execution_report.xlsx",
    index=False
)

print(
    "\nExecution report saved to output/execution_report.xlsx"
)