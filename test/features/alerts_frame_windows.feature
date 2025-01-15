Feature: TP exploration of the alerts, frame and windows
    User wants to check Windows browsers
    as well as the opening of a modal

    Scenario: Open new tab and close the window
        Given I am on the home page
        When I navigate to the "Alerts, Frame & Windows" section
        And I open a new tab and I close the newly opened tab
        Then I verify close the newly opened tab

    Scenario: Verify "lorem ipsum" in large modal dialog
        Given I am on the home page
        When I navigate to the "Alerts, Frame & Windows" section
        And I open the "Modal dialogs" section
        And I open the large modal dialog
        Then I should see "lorem ipsum" 4 times in the large modal dialog