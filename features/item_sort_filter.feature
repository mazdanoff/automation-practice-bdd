Feature: Item sorting and filtering

  Scenario Outline: Item filtering
    Given 'WOMEN' category page is displayed
    And there are 7 items available
    When I filter by '<option>' in '<filter>'
    Then there are <amount> items available

    Examples:
    | filter       | option   | amount |
    | Categories   | Tops     | 2      |
    | Size         | L        | 7      |
    | Color        | Orange   | 3      |
    | Availability | In stock | 5      |
