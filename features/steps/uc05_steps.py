from datetime import datetime
from behave import given, when, then


# ---------- helpers (the tiny fake "app") ----------

def _pending(context):
    return [d for d, n in context.needs.items() if n["status"] == "Pending Review"]


def _select(context, description):
    context.queue = _pending(context)
    assert description in context.queue, f"'{description}' not in review queue"
    context.selected = description


def _log(context, need_name, decision, reason=None):
    context.decisions.append({
        "need": need_name,
        "decision": decision,
        "moderator": "Moderator 1",
        "time": datetime.now(),
        "reason": reason,
    })


def _refresh_queue(context):
    context.queue = _pending(context)
    context.queue_refreshed = True


# ---------- Given ----------

@given('the Moderator is logged in with the Moderator role')
def step_moderator_logged_in(context):
    context.is_moderator = True
    context.needs = {}
    context.queue = []
    context.selected = None
    context.errors = set()
    context.decisions = []
    context.queue_refreshed = False


@given('the need "{description}" has the status "{status}"')
def step_need_has_status(context, description, status):
    context.needs[description] = {
        "status": status, "reason": None, "published": False, "notified": None,
    }


@given('the Moderator has selected the need "{description}"')
def step_given_selected(context, description):
    _select(context, description)


@given('another Moderator has already processed the need "{description}"')
def step_other_moderator(context, description):
    context.needs[description]["status"] = "Verified"
    context.needs[description]["published"] = True


# ---------- When ----------

@when('the Moderator opens the review queue')
def step_open_queue(context):
    context.queue = _pending(context)


@when('the Moderator selects the need "{description}"')
def step_select(context, description):
    _select(context, description)


@when('the Moderator approves the need')
def step_approve(context):
    need = context.needs[context.selected]
    if need["status"] != "Pending Review":          # A3
        context.errors.add("already_processed")
        _refresh_queue(context)
        return
    need["status"] = "Verified"
    need["published"] = True
    need["notified"] = "approved"
    _log(context, context.selected, "approved")


@when('the Moderator rejects the need with the reason "{reason}"')
def step_reject_with_reason(context, reason):
    context.errors.discard("reason")
    need = context.needs[context.selected]
    need["status"] = "Rejected"
    need["reason"] = reason
    need["published"] = False
    need["notified"] = f"rejected: {reason}"
    _log(context, context.selected, "rejected", reason)


@when('the Moderator rejects the need without a reason')
def step_reject_without_reason(context):
    context.errors.add("reason")                     # A2: nothing changes


# ---------- Then ----------

@then('the review queue lists the need "{description}"')
def step_queue_lists(context, description):
    assert description in context.queue


@then('the review queue no longer lists the need "{description}"')
def step_queue_not_lists(context, description):
    assert description not in context.queue


@then('the system shows the details, the evidence and the location of the need')
def step_shows_details(context):
    assert context.selected is not None


@then('the need "{description}" now has the status "{status}"')
def step_now_has_status(context, description, status):
    assert context.needs[description]["status"] == status


@then('the need is published on the map')
def step_published(context):
    assert context.needs[context.selected]["published"] is True


@then('the need is not published on the map')
def step_not_published(context):
    assert context.needs[context.selected]["published"] is False


@then('the Reporter is notified that the need was approved')
def step_notified_approved(context):
    assert context.needs[context.selected]["notified"] == "approved"


@then('the Reporter is notified of the rejection with the reason "{reason}"')
def step_notified_rejected(context, reason):
    assert context.needs[context.selected]["notified"] == f"rejected: {reason}"


@then('the reason "{reason}" is saved')
def step_reason_saved(context, reason):
    assert context.needs[context.selected]["reason"] == reason


@then('the decision is logged with the Moderator and the time')
def step_decision_logged(context):
    entry = context.decisions[-1]
    assert entry["moderator"] and entry["time"]


@then('the system asks for a reason and does not continue')
def step_asks_reason(context):
    assert "reason" in context.errors


@then('the system informs the Moderator that the need has already been processed')
def step_already_processed(context):
    assert "already_processed" in context.errors


@then('the review queue is refreshed')
def step_queue_refreshed(context):
    assert context.queue_refreshed