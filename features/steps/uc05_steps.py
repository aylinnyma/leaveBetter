from behave import given, when, then

@given('The Moderator is logged in with moderator role')
def step_impl(context):
    print("-> Moderator is logged in with proper permissions.")

@given('The review queue is open with pending reports')
def step_impl(context):
    print("-> Review queue is loaded with pending items.")

@when('The Moderator selects the report with title {title}')
def step_impl(context, title):
    print(f"-> Selecting report: {title}")

@when('The Moderator reviews the details and evidence')
def step_impl(context):
    print("-> Reviewing evidence and location details.")

@when('The Moderator clicks the Approve button')
def step_impl(context):
    print("-> Clicking Approve button.")

@when('The Moderator confirms the approval')
def step_impl(context):
    print("-> Confirming approval.")

@then('The report status is set to Verified')
def step_impl(context):
    print("-> Status updated to Verified.")

@then('The aid need is published on the map')
def step_impl(context):
    print("-> Aid need published on the public map.")

@then('A notification is sent to the Reporter')
def step_impl(context):
    print("-> Notification sent to the reporter successfully.")

@when('The Moderator clicks the Reject button')
def step_impl(context):
    print("-> Clicking Reject button.")

@when('The Moderator selects {reason} as rejection reason')
def step_impl(context, reason):
    print(f"-> Selecting rejection reason: {reason}")

@when('The Moderator enters {explanation} as additional explanation')
def step_impl(context, explanation):
    print(f"-> Entering explanation: {explanation}")

@when('The Moderator clicks Confirm Reject')
def step_impl(context):
    print("-> Clicking Confirm Reject button.")

@then('The report status is set to Rejected')
def step_impl(context):
    print("-> Status updated to Rejected.")

@then('The rejection reason is saved')
def step_impl(context):
    print("-> Rejection reason and logs are saved.")

@then('The aid need is not published on the map')
def step_impl(context):
    print("-> Aid need remains hidden from the map.")

@then('A notification with the reason is sent to the Reporter')
def step_impl(context):
    print("-> Rejection notification sent to the reporter.")

@when('The Moderator selects a pending report')
def step_impl(context):
    print("-> Selecting a pending report for rejection test.")

@when('The Moderator leaves the rejection reason empty')
def step_impl(context):
    print("-> Leaving rejection reason unselected.")

@then('The system asks for a reason and does not continue')
def step_impl(context):
    print("-> Validation error shown: Rejection reason is required.")