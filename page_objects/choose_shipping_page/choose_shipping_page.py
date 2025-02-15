from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.checkbox import Checkbox
from page_objects.abstract.web_elements.text import Text
from page_objects.choose_shipping_page.choose_shipping_page_locators import ChooseShippingPageLocators as Locators

class ChooseShippingPage(AbsBasePage):

    header = Text(Locators.HEADER)
    terms_of_service = Checkbox(Locators.TERMS_OF_SERVICES)
    proceed_to_checkout = Button(Locators.PROCEED_TO_CHECKOUT)
    notification_popup = Text(Locators.NOTIFICATION_POPUP, wait_con=visibility_of_element_located)

    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text == "SHIPPING:"

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_for_presence_of_element_located(self.terms_of_service.locator)
