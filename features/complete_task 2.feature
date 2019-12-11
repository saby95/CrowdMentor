Feature: Worker can claim and complete tasks

    Scenario: Worker can claim tasks
        Given I am an existing user with worker access
        And I am logged in as the user with worker access
        And there is an open task
        Then I can claim the task
        
    Scenario: Worker can complete the claimed task
        Given I am an existing user with worker access
        And I am logged in as the user with worker access
        And I have claimed a task
        Then I can complete the task

