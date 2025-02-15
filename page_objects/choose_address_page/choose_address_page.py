from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.dropdown import Dropdown
from page_objects.abstract.web_elements.text import Text
from page_objects.choose_address_page.choose_address_page_locators import ChooseAddressPageLocators as Locators

class ChooseAddressPage(AbsBasePage):

    header = Text(Locators.HEADER)
    my_address = Dropdown(Locators.MY_ADDRESS)
    proceed_to_checkout = Button(Locators.PROCEED_TO_CHECKOUT)

    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text == "ADDRESSES"

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_until(self.is_page_displayed, timeout=timeout)
