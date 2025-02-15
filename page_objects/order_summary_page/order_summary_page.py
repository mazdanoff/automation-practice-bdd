from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.button import Button
from page_objects.order_summary_page.order_summary_page_locators import OrderSummaryPageLocators as Locators

class OrderSummaryPage(AbsBasePage):

    confirm_order_button = Button(Locators.CONFIRM_ORDER_BUTTON)

    def is_page_displayed(self):
        return self.confirm_order_button.is_displayed()

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(self.confirm_order_button.locator, timeout)
