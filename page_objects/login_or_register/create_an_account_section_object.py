from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.abstract.form_object_mixin import FormObjectMixin
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.input_field import InputField
from page_objects.login_or_register.create_an_account_section_object_locators import CreateAnAccountObjectLocators as Locators

class CreateAnAccountSection(AbsPageObject, FormObjectMixin):

    email_address = InputField(Locators.EMAIL_FIELD)
    sign_in = Button(Locators.SIGN_IN)

    @property
    def submit_button(self):
        return self.sign_in.element
