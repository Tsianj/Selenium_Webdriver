Feature: TP exploration of the elements 
    The user wants to explore the check boxes
    and web tables

    Scenario: Select a check box list
        Given I am on the home page
        When I go to the "check box" page
        Then I verify the check boxes are correctly selected

    Scenario: Modify web tables
        Given I am on the home page
        When I go to the "web tables" page
        And I delete the last two rows
        And I modify the salary of the remaining row to 4300
        Then I verify the salary is updated to 4300