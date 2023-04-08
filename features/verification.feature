Feature: User Verification during Registration

    Scenario: Successful Registration

        Given A new user wants to register for UvicAnon with valid username
        When The user submits registration form
        Then The user is routed to the verification page

    Scenario: Unsuccessful Registration

        Given A new user wants to register for UvicAnon with invalid username
        When The user submits registration form
        Then The username fails form validation