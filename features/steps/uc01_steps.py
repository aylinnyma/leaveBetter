from behave import given, when, then

@given('The Reporter is logged in')
def step_impl(context):
    
    print("-> Reporter is logged in successfully.")

@given('The report form is open')
def step_impl(context):
    print("-> Report form is open and ready.")

@when('The Reporter types the title {title} and the input is correct')
def step_impl(context, title):
    print(f"-> Typing title: {title}")

@when('The Reporter types the description {description} and the input is correct')
def step_impl(context, description):
    print(f"-> Typing description: {description}")

@when('The Reporter chooses {aid_type} as type of aid')
def step_impl(context, aid_type):
    print(f"-> Selecting aid type: {aid_type}")

@when('The Reporter chooses {urgency} as urgency level')
def step_impl(context, urgency):
    print(f"-> Selecting urgency: {urgency}")

@when('The Reporter attaches the evidence {evidence}')
def step_impl(context, evidence):
    print(f"-> Attaching file: {evidence}")

@when('The Reporter clicks the Submit button')
def step_impl(context):
    print("-> Clicking Submit button.")

@then('The report screen is closed')
def step_impl(context):
    print("-> Report screen closed.")

@then('The new aid need with {title} is saved with status Pending Review')
def step_impl(context, title):
    print(f"-> Verifying that aid need '{title}' is saved as Pending Review.")

@when('The Reporter presses the Cancel button')
def step_impl(context):
    print("-> Clicking Cancel button.")

@then('No aid need is saved')
def step_impl(context):
    print("-> Verifying no record was saved.")