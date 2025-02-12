from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.text import Text
from page_objects.login_or_register.already_registered_section_object import AlreadyRegisteredSection
from page_objects.login_or_register.create_an_account_section_object import CreateAnAccountSection
from page_objects.login_or_register.login_or_register_page_locators import LoginOrRegisterPageLocators as Locators


class LoginOrRegisterPage(AbsBasePage):

    header = Text(Locators.HEADER)
    alert_notification = Text(Locators.ALERT_NOTIFICATION)

    def __init__(self, driver, url: str = None):
        super(LoginOrRegisterPage, self).__init__(driver, url)
        self.create_an_account = CreateAnAccountSection(driver)
        self.already_registered = AlreadyRegisteredSection(driver)

    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text == "AUTHENTICATION"

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(self.header.locator)
        self.wait_for_visibility_of_element_located(self.create_an_account.email_address.locator)
        self.wait_for_visibility_of_element_located(self.already_registered.email_address.locator)
