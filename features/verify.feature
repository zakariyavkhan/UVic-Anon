@verify
Feature: User Verification during Registration

    Scenario: Successful Registration

        Given A new user wants to register for UvicAnon with valid username
        When The user submits registration form
        Then The user is routed to the verification page

    Scenario: Invalid NetlinkID

        Given A new user wants to register for UvicAnon with invalid username
        When The user submits registration form
        Then The username not a NetlinkID

    Scenario: User Already Exists

        Given A user tries to register with in use NetlinkID
        When The user submits registration form
        Then The username already associated with user
