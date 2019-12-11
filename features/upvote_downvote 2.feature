Feature: Workers can upvote and downvote questions and answers

    Scenario: Worker thinks a question is good and wants to upvote it
        Given there exists a question
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        Then I can upvote the question

     Scenario: Worker thinks a question is bad and wants to downvote it
        Given there exists a question
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I downvote once
        Then I can downvote the question
 
    Scenario: Worker thinks an answer is good and wants to upvote it
        Given there exists a question with an answer
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I upvote once
        Then I can upvote the answer
 
    Scenario: Worker thinks an answer is bad and wants to downvote it
        Given there exists a question with an answer
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        Then I can downvote the answer

    Scenario: Worker can remove an upvote
        Given there exists a question
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click the upvote even number of times
        Then I can remove upvote a question

    Scenario: Worker can remove an downvote
        Given there exists a question
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click the downvote even number of times
        Then I can remove downvote a question

    Scenario: Worker can add an upvote by clicking odd number of times
        Given there exists a question
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click the upvote odd number of times
        Then I will upvote a question

    Scenario: Worker can remove an downvote by clicking odd number of times
        Given there exists a question
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click the downvote odd number of times
        Then I will downvote a question

    Scenario: Worker can remove an upvote by clicking downvote
        Given there exists a question
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click upvote and then downvote
        Then I can remove upvote a question

    Scenario: Worker can remove an downvote by clicking upvote
        Given there exists a question
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click downvote and then upvote
        Then I can remove upvote a question




    Scenario: Worker can remove an upvote of an answer
        Given there exists a question with an answer
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click the upvote even number of times the answer
        Then I can remove upvote an answer

    Scenario: Worker can remove an downvote of an answer
        Given there exists a question with an answer
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click the downvote even number of times the answer
        Then I can remove downvote an answer

    Scenario: Worker can add an upvote an answer by clicking odd number of times
        Given there exists a question with an answer
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click the upvote odd number of times the answer
        Then I will upvote an answer

    Scenario: Worker can remove an downvote an answer by clicking odd number of times
        Given there exists a question with an answer
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I click the downvote odd number of times the answer
        Then I will downvote an answer

    Scenario: Worker can remove an upvote of an answer by clicking downvote
        Given there exists a question with an answer
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I on the answer type click upvote and then downvote
        Then I can remove upvote an answer

    Scenario: Worker can remove an downvote of an answer by clicking upvote
        Given there exists a question with an answer
        And I am an existing user with worker access
        And I am logged in as the user with worker access
        When I on the answer type click downvote and then upvote
        Then I can remove upvote an answer