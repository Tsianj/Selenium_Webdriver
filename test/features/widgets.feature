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
        And I navigate through the menu to select "Sub Sub Item 2"
        Then "Sub Sub Item 2" should be displayed as selected
      
    Scenario: Select various options in the Select Menu
        Given I am on the home page
        When I navigate to the "Widgets" section
        And I configure the select menus with the required options
        Then I should see the options reflected correctly