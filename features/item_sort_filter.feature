Feature: Item sorting and filtering
  """
  Tests related to using sort and filter features on product category pages.
  Cases in short:
  - single filtering
  - sorting
  - combining filters from the same set of options (i.e. Tops and Dresses in Categories)
  - combining filters from different sets of options (i.e. Tops from Categories and Black from Color)
  """
  # CANDIDATE NOTE:
  # I noticed that there are some issues with statuses related to being in stock for products.
  # I made sure to bring the issues into light with a few test cases. I assume this is deliberately prepared
  # to emulate finding issues, but noting just in case: there will be fails.

  Scenario Outline: Item filtering
    Given 'WOMEN' category page is displayed
    And there are 7 items listed
    When I filter by '<option>' in '<filter>'
    Then there are <amount> items listed

    Examples:
    | filter       | option        | amount |
    | Categories   | Tops          | 2      |
    | Categories   | Dresses       | 5      |
    | Size         | M             | 7      |
    | Size         | L             | 7      |
    | Color        | Orange        | 3      |
    | Color        | Blue          | 2      |
    | Availability | In stock      | 5      |
    | Availability | Not available | 2      |

  Scenario Outline: Item sorting
    Given 'WOMEN' category page is displayed
    And there are 7 items listed
    When I sort by <option>
    Then items are sorted <specifically>

    Examples:
    | option               | specifically                                      |
    | Product Name: A to Z | alphabetically                                    |
    | Product Name: Z to A | alphabetically in reverse                         |
    | Price: Lowest first  | by price with lowest first                        |
    | Price: Highest first | by price with highest first                       |
    | In stock             | with out of stock items pushed to the list bottom |

  Scenario Outline: Combining same category filters
    """This should list items that are within option1 OR option2,
       requiring both to be true would return an empty set,
       as i.e. no item is both a top and a dress"""
    Given 'WOMEN' category page is displayed
    And there are 7 items listed
    When I filter by '<option1>' in '<filter>'
    And I filter by '<option2>' in '<filter>'
    Then there are <amount> items listed

    Examples:
    | filter       | option1       | option2        | amount |
    | Categories   | Tops          | Dresses        | 7      |
    | Color        | White         | Beige          | 3      |


  Scenario Outline: Combining different category filters
    """This should list items that are within option1 AND option2,
       as items can have multiple traits, i.e. be a black top"""
    Given 'WOMEN' category page is displayed
    And there are 7 items listed
    When I filter by '<option1>' in '<filter1>'
    And I filter by '<option2>' in '<filter2>'
    Then there are <amount> items listed

    Examples:
    | filter1      | option1       | filter2      |  option2        | amount |
    | Categories   | Tops          | Color        |  Black          | 1      |
    | Categories   | Dresses       | Color        |  Orange         | 2      |
    | Categories   | Dresses       | Availability |  In stock       | 4      |
    | Color        | Orange        | Availability |  In stock       | 1      |