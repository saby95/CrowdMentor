Feature: Change role form

  Scenario: Access the change role form

    Given I am an existing user with admin access
    And there is one user with worker access
    And I am logged in as the user with admin access
    When I change any user role
    Then I am redirected to the home page
