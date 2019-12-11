Feature: Add task form

  Scenario: Access the add task form
    Given I am an existing user with task_updater access
    And I am logged in as the user with task_updater access
    When I give valid task
    Then I am redirected to the task page

  Scenario: User cannot add task
    Given I am an existing user with worker access
    And I am logged in as the user with worker access
    When I try to add a task
    Then I get error saying permission denied

  Scenario: View the detail of a task
    Given A task has been submitted
    And I am an existing user with worker access
    And I am logged in as the user with worker access
    Then I can view the details of a task

