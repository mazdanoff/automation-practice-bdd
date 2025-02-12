from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.form_object_mixin import FormObjectMixin
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.input_field import InputField
from page_objects.abstract.web_elements.text import Text
from page_objects.create_an_account.create_an_account_page_locators import CreateAnAccountPageLocators as Locators

class CreateAnAccountPage(AbsBasePage, FormObjectMixin):

    header = Text(Locators.HEADER)
    email_address = InputField(Locators.EMAIL_FIELD)
    register = Button(Locators.REGISTER)

    def is_page_displayed(self):
        return self.header.is_displayed() and self.header.text == "CREATE AN ACCOUNT"

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_text_to_be_present_in_element_located(Locators.HEADER,
                                                            "CREATE AN ACCOUNT")

    @property
    def submit_button(self):
        return self.register.element
