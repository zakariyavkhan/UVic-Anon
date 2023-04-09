@anonymity
Feature: Hide usernames on homepage when user is logged in

  Scenario: User visits home page and sees no usernames
    Given A user is logged in
    When The user visits the home page
    Then No usernames will be visible