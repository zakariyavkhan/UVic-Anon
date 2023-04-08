Feature: User Verification during Registration

    Scenario: Successful Registration

        Given A new user registers for UvicAnon with valid username
        When The user submits registration form
        Then A verification email is sent to the netlinkid

    Scenario: Unsuccessful Registration

        Given A new user registers for UvicAnon with invalid username
        When The user submits registration form
        Then The username fails form validation