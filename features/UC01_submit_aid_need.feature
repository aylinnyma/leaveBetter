Feature: UC1 Submit aid need with evidence
  As a Reporter
  I want to submit a community aid need with evidence
  So that a Moderator can review it before volunteers can see it

  Background:
    Given the Reporter is registered and logged in
    And the Reporter has opened the report form

  @uc1-feature
  Scenario Outline: Basic flow - submit a valid aid need
    When the Reporter enters the description "<description>"
    And the Reporter selects "<category>" as category
    And the Reporter attaches the evidence "<evidence>"
    And the Reporter submits the form
    Then the system geotags the location of the need
    And the aid need "<description>" is saved with status "Pending Review"
    And the aid need is not visible on the public map
    And the Reporter is notified that the need is waiting for moderation

    Examples: Aid needs
      | description              | category  | evidence  |
      | Main well pump is broken | Water     | proof.jpg |
      | Notebooks and pens       | Education | doc.pdf   |

  @uc1-feature
  Scenario: A1 - Required field missing, then corrected
    When the Reporter leaves the description empty
    And the Reporter selects "Food" as category
    And the Reporter submits the form
    Then an error is shown next to the description field
    And no aid need is saved
    When the Reporter enters the description "Family needs food packages"
    And the Reporter submits the form
    Then the aid need "Family needs food packages" is saved with status "Pending Review"

  @uc1-feature
  Scenario: A2 - Evidence file not accepted, then replaced
    When the Reporter attaches the evidence "virus.exe"
    Then the system rejects the file and explains the file type is not supported
    When the Reporter attaches the evidence "proof.jpg"
    And the Reporter enters the description "Roof damaged after storm"
    And the Reporter selects "Construction" as category
    And the Reporter submits the form
    Then the aid need "Roof damaged after storm" is saved with status "Pending Review"

  @uc1-feature
  Scenario: A3 - Location could not be determined
    Given the location of the need cannot be determined
    When the Reporter enters the description "Main well pump is broken"
    And the Reporter selects "Water" as category
    And the Reporter attaches the evidence "proof.jpg"
    And the Reporter submits the form
    Then the Reporter is informed that the location could not be determined
    And no aid need is saved

  @uc1-feature
  Scenario: A4 - Reporter cancels the form
    When the Reporter enters the description "Main well pump is broken"
    And the Reporter cancels the form
    Then no aid need is saved
    And the report form is closed
