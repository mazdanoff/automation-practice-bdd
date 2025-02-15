from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.text import Text
from page_objects.order_confirmation_page.order_confirmation_page_locators import OrderConfirmationPageLocators as Locators

class OrderConfirmationPage(AbsBasePage):

    header = Text(Locators.HEADER)
    alert_notification = Text(Locators.ALERT)

    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text == "ORDER CONFIRMATION"

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(self.alert_notification.locator, timeout)
