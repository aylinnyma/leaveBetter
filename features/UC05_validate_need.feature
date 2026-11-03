Feature: Use Case 5 Validate need
  As a Moderator
  I want to review pending reports and validate or reject them
  Therefore I want the fields: review queue, approval action, rejection reason and explanation able to be processed

  Background:
    Given The Moderator is logged in with moderator role
    And The review queue is open with pending reports

  @uc5-feature
  Scenario Outline: Successfully approve a pending aid need
    When The Moderator selects the report with title <title>
    And The Moderator reviews the details and evidence
    And The Moderator clicks the Approve button
    And The Moderator confirms the approval
    Then The report status is set to Verified
    And The aid need is published on the map
    And A notification is sent to the Reporter

    Examples: Approved Reports
      | title                   |
      | Food and water needed   |
      | Medical supplies        |

  @uc5-feature
  Scenario Outline: Reject a pending aid need with a reason
    When The Moderator selects the report with title <title>
    And The Moderator clicks the Reject button
    And The Moderator selects <reason> as rejection reason
    And The Moderator enters <explanation> as additional explanation
    And The Moderator clicks Confirm Reject
    Then The report status is set to Rejected
    And The rejection reason is saved
    And The aid need is not published on the map
    And A notification with the reason is sent to the Reporter

    Examples: Rejected Reports
      | title              | reason              | explanation                   |
      | Education materials| Incomplete evidence | Photos do not show clear proof|
      | Fake Report Sample | Spam or Fraudulent  | This is a duplicate submission|

  @uc5-feature
  Scenario: Attempting to reject a report without a reason
    When The Moderator selects a pending report
    And The Moderator clicks the Reject button
    And The Moderator leaves the rejection reason empty
    And The Moderator clicks Confirm Reject
    Then The system asks for a reason and does not continue