from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.abstract.form_object_mixin import FormObjectMixin
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.input_field import InputField
from page_objects.abstract.web_elements.text import Text
from page_objects.login_or_register.create_an_account_section_object_locators import CreateAnAccountObjectLocators as Locators

class CreateAnAccountSection(AbsPageObject, FormObjectMixin):

    email_address = InputField(Locators.EMAIL_FIELD)
    create_an_account = Button(Locators.CREATE_AN_ACCOUNT)
    alert_notification = Text(Locators.ALERT_NOTIFICATION, wait_con=visibility_of_element_located)

    @property
    def submit_button(self):
        return self.create_an_account.element
