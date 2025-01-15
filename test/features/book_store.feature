Feature: TP exploration of the book store

  Scenario: Search for a book by Marijn Haverbeke
    Given I am on the home page
    When I navigate to the "Book Store Application" section
    And I search for "Marijn Haverbeke" in the book store
    Then I should see the book by "Marijn Haverbeke" displayed