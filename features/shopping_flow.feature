Feature: Shopping flow

  Scenario: Basic flow
    #TODO: 1. Come up with a solution to provide address beforehand
    #TODO: 2. Add handling of address form popping up in the middle of shopping flow
    Given YourLogo main page is displayed
    # And I'm logged in
    # And I have provided my address beforehand

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
    And I'm logged in

    When I type 'summer' into the search bar
    And I click the search button

    Then the Search page is displayed
    And the first item's name includes a 'Summer' word

  Scenario: Using search hints
    Given YourLogo main page is displayed
    And I'm logged in

    When I type 'Blouse' into the search bar
    And I choose the search bar's first hint

    Then a product page is displayed
    And the product's name is 'Blouse'