Feature: Login form

  Scenario: Existing user accesses the login form with the correct credentials
    Given I am an existing user who tries to access the site
    When I submit a valid login page
    Then I am redirected to the home page

  Scenario: Existing user accesses the login form with the incorrect credentials
    Given I am an existing user who tries to access the site
    When I submit an invalid login page
    Then I get an error message saying that my username and password did not match.
