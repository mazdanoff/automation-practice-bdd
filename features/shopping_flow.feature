Feature: Shopping flow
  """
  This test suite covers:
  - basic flow, from main page, through picking products, cart summary
    and payments screens up to order confirmation
  - search bar
  - menu options in cart summary screen
  - cart preview in top navigation
  - attempt to avoid agreeing to terms of services
  """

  Scenario: Basic flow
    Given YourLogo main page is displayed

    When I go to 'Tops' category
    And I pick the 'Blouse' item
    And I choose size 'L'
    And I choose white color
    And I choose quantity of 2
    And I click 'Add to cart' button and proceed to checkout
    And I proceed to checkout on cart summary page
    And I sign in
    And I choose my delivery address
    And I choose shipping and agree to terms of service
    And I choose payment by bank-wire
    And I confirm my order

    Then Order Confirmation page is displayed
    And a 'Your order on My Shop is complete.' message is displayed

  Scenario: Using search
    Given YourLogo main page is displayed

    When I type 'summer' into the search bar
    And I click the search button

    Then the Search page for 'summer' is displayed
    And the first item's name includes a 'Summer' word

  Scenario: Using search hints
    Given YourLogo main page is displayed

    When I type 'Blouse' into the search bar
    And I choose the search bar's first hint

    Then a product page is displayed
    And the product's name is 'Blouse'

  Scenario: Cannot proceed past shipping without accepting terms of service
    Given YourLogo main page is displayed
    And I'm logged in

    And I go to 'Tops' category
    And I pick the 'Blouse' item
    And I choose size 'L'
    And I choose white color
    And I choose quantity of 2
    And I click 'Add to cart' button and proceed to checkout
    And I proceed to checkout on cart summary page
    And I choose my delivery address

    When I try to proceed through shipping page without accepting terms of service

    Then a notification pops up on shipping page
    And the message says 'You must agree to the terms of service before continuing.'

  Scenario Outline: Total price changes when altering quantity on cart summary page
    Given YourLogo main page is displayed
    And I'm logged in
    And I go to 'Tops' category
    And I pick the 'Blouse' item
    And I choose size 'L'
    And I choose white color
    And I choose quantity of 2
    And I click 'Add to cart' button and proceed to checkout

    When I <change> quantity by <amount> in cart

    Then quantity changes to <result_amount>
    And total price changes to <total>

    Examples:
    | change   | amount | result_amount | total |
    | decrease | 1      | 1             | $34   |
    | increase | 1      | 3             | $88   |
    | increase | 2      | 4             | $115  |

  Scenario: Cart preview
    Given YourLogo main page is displayed
    And I'm logged in
    And I go to 'Tops' category
    And I pick the 'Blouse' item
    And I choose size 'L'
    And I choose white color
    And I choose quantity of 2
    And I click 'Add to cart' button and proceed to checkout

    When I hover over cart icon in top navigation

    Then a cart preview is shown
    And there's 'Blouse' item with a quantity of 2

  # further ideas
  Scenario: Emptying cart from cart preview reverses to shopping cart summary page
  Scenario: Decreasing product quantity to 0 changes view in shopping cart summary page
  Scenario: Basic flow when user did not provide their address beforehand
    #TODO: 1. Come up with a solution to provide address beforehand
    #TODO: 2. Add handling of address form popping up in the middle of shopping flow