from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.text import Text
from page_objects.search_page.search_page_locators import SearchPageLocators as Locators
from page_objects.product_list import ProductList


class SearchPage(AbsBasePage):

    header = Text(Locators.HEADER)
    product_list = ProductList(*Locators.ITEM_LIST)

    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text.startswith("SEARCH")

    def wait_for_page_to_load(self, timeout: int = 10):
        self.wait_until(self.is_page_displayed, timeout=timeout)
