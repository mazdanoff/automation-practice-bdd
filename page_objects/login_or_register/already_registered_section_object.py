from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.abstract.form_object_mixin import FormObjectMixin
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.input_field import InputField
from page_objects.login_or_register.already_registered_section_object_locators import \
    AlreadyRegisteredObjectLocators as Locators


class AlreadyRegisteredSection(AbsPageObject, FormObjectMixin):

    email_address = InputField(Locators.EMAIL_FIELD)
    password = InputField(Locators.PASSWD_FIELD)
    sign_in = Button(Locators.SIGN_IN)

    @property
    def submit_button(self):
        return self.sign_in.element
