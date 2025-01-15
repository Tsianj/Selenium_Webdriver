Feature: TP exploration of the elements 
    The user wants to explore the check boxes
    and web tables

    Scenario: Select a check box list
        Given I am on the home page
        When I go to the "check box" page
        Then I verify the check boxes are correctly selected

    Scenario: Modify web tables
        Given I am on the home page
        When I adjust the web table by removing rows and updating a salary
        Then the salary of the remaining row should be 4300