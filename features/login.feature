Feature: Login
  """Tests covering functionalities related to signing in on YourLogo store.
  Cases in short:
  - successful login (happy path)
  - unsuccessful login due to a wrong password
  - highlighting email/password correct formatting
  - highlighting email/password incorrect formatting
  - various alerts
  - redirection to login page"""

  Scenario: Happy Path
    """Key notes:
    - visible 'Sign in' button is indicating no user is logged in
    - visible 'Sign out' button is indicating a user is signed in
    - the user account name matches the expected user (here: Romuald Mean)"""

    Given YourLogo main page is displayed
    * there's a 'Sign in' button in top navigation bar

    When I click a 'Sign in' button in the top navigation bar
    And I input my credentials in 'Already registered' section
    And I click the green 'Sign in' button

    Then 'My Account' page is displayed
    And there's a 'Sign out' button in the top navigation bar
    And my name is displayed in the top navigation bar


  Scenario: Logging in using a wrong password for an existing user
    Given YourLogo main page is displayed
    And I click a 'Sign in' button in the top navigation bar

    When I input credentials with a wrong password
    And I click the green 'Sign in' button

    Then Login page is displayed
    And an 'Authentication failed.' alert is displayed


  Scenario: A correct email format is highlighted in green
    Given YourLogo main page is displayed
    And I click a 'Sign in' button in the top navigation bar

    When I input credentials with correctly formatted email

    Then the email address field is highlighted in green
    And an OK icon is displayed in the email address field


  Scenario: An incorrect email format is highlighted in red
    Given YourLogo main page is displayed
    And I click a 'Sign in' button in the top navigation bar

    When I input credentials with incorrectly formatted email

    Then the email address field is highlighted in red
    And an X icon is displayed in the email address field


  Scenario Outline: A password with at least 5 characters is highlighted in green
    Given YourLogo main page is displayed
    And I click a 'Sign in' button in the top navigation bar

    When I input credentials with password of length of <n>

    Then the password field is highlighted in green
    And an OK icon is displayed in the password field
    Examples:
      | n |
      | 5 |
      | 6 |


  Scenario Outline: A password with at most 4 characters is highlighted in red
    Given YourLogo main page is displayed
    And I click a 'Sign in' button in the top navigation bar

    When I input credentials with password of length of <n>

    Then the password field is highlighted in red
    And an X icon is displayed in the password field
    Examples:
      | n |
      | 4 |
      | 3 |


  Scenario: An incorrect email format is not accepted by the Login page
    Given YourLogo main page is displayed
    And I click a 'Sign in' button in the top navigation bar

    When I input credentials with incorrectly formatted email
    And I click the green 'Sign in' button

    Then Login page is displayed
    And an 'Invalid email address.' alert is displayed


  Scenario: A too short password is not accepted by the Login page
    Given YourLogo main page is displayed
    And I click a 'Sign in' button in the top navigation bar

    When I input credentials with password of length of 3
    And I click the green 'Sign in' button

    Then Login page is displayed
    And an 'Invalid password.' alert is displayed


  Scenario: Redirection of non-signed user to Login page
    Given YourLogo main page is displayed
    * there's a 'Sign in' button in top navigation bar

    When I attempt to open 'My Account' page by url

    Then Login page is displayed
    And My Account page is not displayed
    And there's a 'Sign in' button in top navigation bar