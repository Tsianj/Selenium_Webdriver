Feature: Contact Form

  Scenario: Verify the presence of the input field
    Given I am on the contact page
    When I fill in the contact form
    Then I should see the "nom" input field "text"