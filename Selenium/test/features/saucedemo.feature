Feature: User authentication on the Saucedemo site

  Scenario: Successful login and logout with a valid user
    Given I am on the login page
    When I authenticate using valid credentials
    Then I should be logged into the system
    When I log out of the system
    Then I should be logged out successfully


  Scenario: Attempt to log in with a locked-out account
    Given I am on the login page
    When I attempt to log in using a locked-out account
    Then I should see an error message indicating the account is locked

