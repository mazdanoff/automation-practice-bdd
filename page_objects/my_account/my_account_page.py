from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.text import Text
from page_objects.my_account.my_account_page_locators import MyAccountPageLocators as Locators


class MyAccountPage(AbsBasePage):

    header = Text(Locators.HEADER)

    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text == "MY ACCOUNT"

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(self.header.locator)
