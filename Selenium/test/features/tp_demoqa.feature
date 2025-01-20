Feature: TP exploration of the DemoQA site
    The user explores the DemoQA site

    Scenario: Select a check box list
        Given I am on the home page
        When I go to the "check box" page
        Then I verify the check boxes are correctly selected
