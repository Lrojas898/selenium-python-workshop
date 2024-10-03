Feature: Login Intu Feature
  Scenario: Successful login with valid credentials
    Given the user is on the intu login page
    When the user logs Intu in with valid credentials
    Then the user should be redirected to the dashboard page