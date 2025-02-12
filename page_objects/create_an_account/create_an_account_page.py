from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.form_object_mixin import FormObjectMixin
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.dropdown import Dropdown
from page_objects.abstract.web_elements.input_field import InputField
from page_objects.abstract.web_elements.text import Text
from page_objects.create_an_account.create_an_account_page_locators import CreateAnAccountPageLocators as Locators

class CreateAnAccountPage(AbsBasePage, FormObjectMixin):

    header = Text(Locators.HEADER)

    first_name = InputField(Locators.FIRST_NAME)
    last_name = InputField(Locators.LAST_NAME)
    email_address = InputField(Locators.EMAIL_FIELD)
    password = InputField(Locators.PASSWORD)
    birth_day = Dropdown(Locators.BIRTH_DAY)
    birth_month = Dropdown(Locators.BIRTH_MONTH)
    birth_year = Dropdown(Locators.BIRTH_YEAR)
    register = Button(Locators.REGISTER)
    alert_notification = Text(Locators.ALERT_NOTIFICATION, wait_con=visibility_of_element_located)


    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text == "CREATE AN ACCOUNT"

    def wait_for_page_to_load(self, timeout: int = 10):
        self.wait_for_text_to_be_present_in_element_located(Locators.HEADER,
                                                            "CREATE AN ACCOUNT")

    @property
    def submit_button(self):
        return self.register.element
