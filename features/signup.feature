Feature: Signup form

  Scenario: New user accesses the signup form
    Given I am a new user who tries to access the site
    When I submit a valid signup page
    Then I am redirected to the home page

  Scenario: Existing user accesses the signup form
    Given I am an existing user who tries to access the site
    When I submit a valid signup page
    Then I get an error message saying that a user with that username already exists.
