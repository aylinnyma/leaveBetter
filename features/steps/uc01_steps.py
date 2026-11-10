from behave import given, when, then
from selenium.webdriver.common.by import By

<<<<<<< HEAD
@given('The Reporter is logged in')
def step_impl(context):

    print("-> Reporter is logged in successfully.")
=======
ALLOWED_TYPES = (".jpg", ".png", ".pdf")
>>>>>>> 6626d1b1980a2227c62061565f330f0bbfe67896


@given('the Reporter is registered and logged in')
def step_logged_in(context):
    context.logged_in = True
    context.saved = []          # needs saved so far
    context.location_ok = True


@given('the Reporter has opened the report form')
def step_form_open(context):
    context.form = {"description": "", "category": None, "evidence": None}
    context.errors = set()
    context.notified = False


@given('the location of the need cannot be determined')
def step_location_fails(context):
    context.location_ok = False


@when('the Reporter enters the description "{description}"')
def step_description(context, description):
    context.form["description"] = description


@when('the Reporter leaves the description empty')
def step_description_empty(context):
    context.form["description"] = ""


@when('the Reporter selects "{category}" as category')
def step_category(context, category):
    context.form["category"] = category


@when('the Reporter attaches the evidence "{evidence}"')
def step_evidence(context, evidence):
    context.errors.discard("evidence")
    if evidence.lower().endswith(ALLOWED_TYPES):
        context.form["evidence"] = evidence
    else:
        context.errors.add("evidence")


@when('the Reporter submits the form')
def step_submit(context):
    context.errors.discard("description")
    context.errors.discard("location")
    if not context.form["description"]:
        context.errors.add("description")
        return
    if not context.location_ok:
        context.errors.add("location")
        return
    context.need = {
        "description": context.form["description"],
        "category": context.form["category"],
        "evidence": context.form["evidence"],
        "location": "geotagged",
        "status": "Pending Review",
    }
    context.saved.append(context.need)
    context.notified = True
    context.form = None          # form closes after a successful submit


@when('the Reporter cancels the form')
def step_cancel(context):
    context.form = None


@then('the system geotags the location of the need')
def step_geotag(context):
    assert context.need["location"] is not None


@then('the aid need "{description}" is saved with status "{status}"')
def step_saved(context, description, status):
    matches = [n for n in context.saved if n["description"] == description]
    assert matches, f"No need saved with description '{description}'"
    assert matches[-1]["status"] == status


@then('the aid need is not visible on the public map')
def step_not_visible(context):
    # Only Verified needs appear on the public map
    assert context.need["status"] != "Verified"


@then('the Reporter is notified that the need is waiting for moderation')
def step_notified(context):
    assert context.notified


@then('an error is shown next to the description field')
def step_error_description(context):
    assert "description" in context.errors


@then('the system rejects the file and explains the file type is not supported')
def step_error_file(context):
    assert "evidence" in context.errors


@then('the Reporter is informed that the location could not be determined')
def step_error_location(context):
    assert "location" in context.errors


@then('no aid need is saved')
def step_nothing_saved(context):
    assert len(context.saved) == 0


@then('the report form is closed')
def step_form_closed(context):
    assert context.form is None
