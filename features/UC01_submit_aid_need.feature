Feature: Use Case 1 Submit aid need with evidence
  As a Reporter
  I want to open the report form and submit a community aid need
  Therefore I want the fields: type of aid, urgency, title, description, location and evidence able to be filled in

  Background:
    Given The Reporter is logged in
    And The report form is open

  @uc1-feature
  Scenario Outline: Successfully submit an aid need with valid inputs
    When The Reporter types the title <title> and the input is correct
    And The Reporter types the description <description> and the input is correct
    And The Reporter chooses <type> as type of aid
    And The Reporter chooses <urgency> as urgency level
    And The Reporter attaches the evidence <evidence>
    And The Reporter clicks the Submit button
    Then The report screen is closed
    And The new aid need with <title> is saved with status Pending Review

    Examples: Aid Needs
      | title           | description              | type      | urgency  | evidence  |
      | Clean Water     | Main well pump is broken | Water     | Critical | proof.jpg |
      | School Supplies | Notebooks and pens       | Education | Medium   | doc.pdf   |

  @uc1-feature
  Scenario: Reporter cancels the report form
    When The Reporter presses the Cancel button
    Then No aid need is saved
    And The report screen is closed