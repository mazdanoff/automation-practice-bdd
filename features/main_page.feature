Feature: Main Page display
  Sanity test to check if the page is even online

  Scenario: Main Page display
    Given I open the browser
    When I open the url 'http://www.automationpractice.pl'
    Then the YourLogo shop's main page is displayed