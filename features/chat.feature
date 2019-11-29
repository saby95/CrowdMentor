Feature: Chat with Mentor

  Scenario: Existing mentor can send message to his workers
    Given there is one user with worker access
    And I am an existing user with mentor access
    And I am mentoring that worker
    And I am logged in as the user with mentor access
    When I send a message to worker
    Then I am redirected to the messages page

  Scenario: Existing worker can send message to his mentor
    Given there is one user with worker access
    And I am an existing user with mentor access
    And I am mentoring that worker
    And I am logged in as the user with worker access
    When I send a message to mentor
    Then I am redirected to the messages page

  Scenario: Existing mentor cannot send empty message to his workers
    Given there is one user with worker access
    And I am an existing user with mentor access
    And I am mentoring that worker
    And I am logged in as the user with mentor access
    When I send an empty message to worker
    Then I get error saying No message found


  Scenario: Worker can see the mentor's message
    Given there is one user with worker access
    And I am an existing user with mentor access
    And I am mentoring that worker
    And I am logged in as the user with mentor access
    When the mentor sends a message to the worker
    Then the worker is able to read the message
    
  Scenario: Mentor can see the worker's message
    Given there is one user with worker access
    And I am an existing user with mentor access
    And I am mentoring that worker
    And I am logged in as the user with worker access
    When the worker sends a message to the mentor
    Then the mentor is able to read the message

