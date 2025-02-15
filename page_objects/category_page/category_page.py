from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.dropdown import Dropdown
from page_objects.category_page.category_page_locators import CategoryPageLocators as Locators
from page_objects.category_page.filters.filter_availability import FilterAvailability
from page_objects.category_page.filters.filter_categories import FilterCategories
from page_objects.category_page.filters.filter_color import FilterColor
from page_objects.category_page.filters.filter_size import FilterSize
from page_objects.product_list.product_list import ProductList


class CategoryPage(AbsBasePage):

    product_list = ProductList(*Locators.ITEM_LIST)
    sort_by = Dropdown(Locators.SORT_BY)

    categories_filter = FilterCategories(*Locators.FILTER_CATEGORIES)
    size_filter = FilterSize(*Locators.FILTER_SIZE)
    color_filter = FilterColor(*Locators.FILTER_COLOR)
    availability_filter = FilterAvailability(*Locators.FILTER_AVAILABILITY)

    def is_page_displayed(self):
        return self.is_element_located_displayed(Locators.ITEM_LIST)

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(Locators.ITEM_LIST)

    def wait_until_item_count_matches(self, expected_amount):
        self.wait_until(lambda: len(self.product_list) == expected_amount)
