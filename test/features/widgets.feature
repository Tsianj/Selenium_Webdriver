Feature: TP exploration of the widgets
    The user will start a progress bar
    as well as menu navigation
    And select various options in the selection menu

    Scenario: Start progress bar and verify completion
        Given I am on the home page
        When I navigate to the "Widgets" section
        And I start the progress bar
        Then I should see the reset button when the progress bar reaches 100%

    Scenario: Navigate to Menu and click on Sub Sub Item 2
        Given I am on the home page
        When I navigate to the "Widgets" section
        And I open the "Menu" section
        And I hover over "Main Item 2" and "Sub Sub List"
        And I click on "Sub Sub Item 2"
        Then I should see "Sub Sub Item 2" is clicked
      
    Scenario: Select various options in the Select Menu
        Given I am on the home page
        When I navigate to the "Widgets" section
        And I open the "Select Menu" section
        And I choose "Another root option" for "Select value"
        And I choose "Other" for "Select one"
        And I choose "Aqua" for "Old style select menu"
        And I choose "Red" and "Black" for "Multi select drop down"
        Then I should see the selected options