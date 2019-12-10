Feature: Workers can ask and answer questions

    Scenario: Worker can ask questions
        Given I am an existing user with worker access
        And I am logged in as the user with worker access
        And I have a question which I need help with
        Then I can post my question

    Scenario: Worker can answer questions
        Given there exists a question
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        Then I can answer the question

       
