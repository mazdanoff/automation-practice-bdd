from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.input_field import InputField
from page_objects.abstract.web_elements.text import Text
from page_objects.shopping_cart_summary.shopping_cart_summary_page_locators import ShoppingCartSummaryPageLocators as Locators

class ShoppingCartSummaryPage(AbsBasePage):

    header = Text(Locators.HEADER)
    proceed_to_checkout = Button(Locators.PROCEED_TO_CHECKOUT)

    # these should be DataTable fields, as cart can have multiple items
    cart_quantity = InputField(Locators.CART_QUANTITY)
    decrease_quantity = Button(Locators.DECREASE_QUANTITY)
    increase_quantity = Button(Locators.INCREASE_QUANTITY)

    total_price = Text(Locators.TOTAL_PRICE)

    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text == "SHOPPING-CART SUMMARY"

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_until(self.is_page_displayed, timeout=timeout)

    def wait_for_quantity_to_change(self, to: str):
        self.wait_until(lambda: self.cart_quantity.value == to, timeout=5)
