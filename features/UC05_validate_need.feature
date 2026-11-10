Feature: UC5 Validate need
  As a Moderator
  I want to review pending needs and approve or reject them
  So that only verified needs are published on the map

  Background:
    Given the Moderator is logged in with the Moderator role

  @uc5-feature
  Scenario Outline: Basic flow - approve a pending need
    Given the need "<description>" has the status "Pending Review"
    When the Moderator opens the review queue
    Then the review queue lists the need "<description>"
    When the Moderator selects the need "<description>"
    Then the system shows the details, the evidence and the location of the need
    When the Moderator approves the need
    Then the need "<description>" now has the status "Verified"
    And the need is published on the map
    And the Reporter is notified that the need was approved
    And the decision is logged with the Moderator and the time

    Examples: Approved needs
      | description              |
      | Food and water needed    |
      | Medical supplies         |

  @uc5-feature
  Scenario Outline: A1 - Moderator rejects the need with a reason
    Given the need "<description>" has the status "Pending Review"
    When the Moderator opens the review queue
    And the Moderator selects the need "<description>"
    And the Moderator rejects the need with the reason "<reason>"
    Then the need "<description>" now has the status "Rejected"
    And the reason "<reason>" is saved
    And the need is not published on the map
    And the Reporter is notified of the rejection with the reason "<reason>"
    And the decision is logged with the Moderator and the time

    Examples: Rejected needs
      | description         | reason                           |
      | Education materials | Photos do not show clear proof   |
      | Fake Report Sample  | Duplicate submission             |

  @uc5-feature
  Scenario: A2 - Rejection reason missing, then entered
    Given the need "Roof damaged" has the status "Pending Review"
    When the Moderator opens the review queue
    And the Moderator selects the need "Roof damaged"
    And the Moderator rejects the need without a reason
    Then the system asks for a reason and does not continue
    And the need "Roof damaged" now has the status "Pending Review"
    When the Moderator rejects the need with the reason "Evidence does not match"
    Then the need "Roof damaged" now has the status "Rejected"

  @uc5-feature
  Scenario: A3 - Need already handled by another Moderator
    Given the need "Water pump broken" has the status "Pending Review"
    And the need "School supplies" has the status "Pending Review"
    And the Moderator has selected the need "Water pump broken"
    And another Moderator has already processed the need "Water pump broken"
    When the Moderator approves the need
    Then the system informs the Moderator that the need has already been processed
    And the review queue is refreshed
    And the review queue no longer lists the need "Water pump broken"
    And the review queue lists the need "School supplies"