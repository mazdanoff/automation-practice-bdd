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

  Scenario Outline: Item sorting
    Given 'WOMEN' category page is displayed
    And there are 7 items available
    When I sort by <option>
    Then items are sorted <specifically>

    Examples:
    | option               | specifically                                      |
    | Product Name: A to Z | alphabetically                                    |
    | Product Name: Z to A | alphabetically in reverse                         |
    | Price: Lowest first  | by price with lowest first                        |
    | Price: Highest first | by price with highest first                       |
    | In stock             | with out of stock items pushed to the list bottom |