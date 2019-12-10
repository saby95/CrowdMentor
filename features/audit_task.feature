Feature: Audit task
    In order to make sure that the tasks are being completed correctly,
    the auditor must be able to audit tasks once the worker completes them.

    Scenario: Auditor must be able to audit a task submitted for audit
        Given there is a task to be audited
        Given I am an existing user with auditor access
        And I am logged in as the user with auditor access
        Then I can claim the task for audit
        And I can audit the task
        
    Scenario: Auditor must be able to see the open audits
        Given there is a task to be audited
        Given I am an existing user with auditor access
        And I am logged in as the user with auditor access
        Then I can view the open audits

    Scenario: Auditor must be able to see the detail of a open audit
        Given there is a task to be audited
        Given I am an existing user with auditor access
        And I am logged in as the user with auditor access
        Then I can view the details of that audit


