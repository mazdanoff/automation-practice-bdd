from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.text import Text
from page_objects.shopping_cary_summary.shopping_cart_summary_page_locators import ShoppingCartSummaryPageLocators as Locators

class ShoppingCartSummaryPage(AbsBasePage):

    header = Text(Locators.HEADER)
    proceed_to_checkout = Button(Locators.PROCEED_TO_CHECKOUT)

    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text == "SHOPPING-CART SUMMARY"

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_until(self.is_page_displayed, timeout=timeout)
