Feature: Register
  Tests covering functionalities related to registering an account on Your Logo site.

  Scenario: Happy Path
#    CANDIDATE NOTE:
#      Because I have no clear way (that I know of) to remove accounts
#      I'm keeping the test function for this case commented out
#      to not clutter the test environment database.
#      The rest of this test suite can be run freely, though.

    Given YourLogo main page is displayed
    * there's a 'Sign in' button in top navigation bar

    When I click a 'Sign in' button in the top navigation bar
    And I input my email address in 'Create an account' section
    And I click a yellow 'Create an account' button
    And I submit the form on 'Create an account' page

    Then 'My account' page is displayed
    And 'Your account has been created.' alert is displayed
    And there's a 'Sign out' button in the top navigation bar
    And my name is displayed in the top navigation bar


  Scenario: A correct email format is highlighted in green
    Given YourLogo main page is displayed
    * there's a 'Sign in' button in top navigation bar

    When I click a 'Sign in' button in the top navigation bar
    And I input my email address in 'Create an account' section

    Then the email address field is highlighted in green
    And an OK icon is displayed in the email address field

  Scenario: An incorrect email format is highlighted in red

  Scenario Outline: Registering an existing account on 'Authentication' page is rejected
    Given YourLogo main page is displayed
    * there's a 'Sign in' button in top navigation bar

    When I click a 'Sign in' button in the top navigation bar
    And I input an email address for an existing account in 'Create an account' section
    And I click a yellow 'Create an account' button

    Then I get an '<message>' alert on Authentication page
    And 'Create an account' page is not displayed

    Examples:
      | message |
      | 'An account using this email address has already been registered. Please enter a valid password or request a new one. ' |


  Scenario Outline: Registering an existing account on 'Create an account' page is rejected
    Given YourLogo main page is displayed
    * there's a 'Sign in' button in top navigation bar

    When I click a 'Sign in' button in the top navigation bar
    And I input an email address for a non-existing account in 'Create an account' section
    And I click a yellow 'Create an account' button
    But I submit the form on 'Create an account' page using an email address for an existing account

    Then I get an '<message>' alert on 'Create an account' page
    And 'My Account' page is not displayed
    And there's a 'Sign out' button in the top navigation bar

    Examples:
      | message |
      | 'An account using this email address has already been registered.' |

  Scenario: Registering using an incorrectly formatted email is rejected
  Scenario: Registration rejected when leaving a required field empty
