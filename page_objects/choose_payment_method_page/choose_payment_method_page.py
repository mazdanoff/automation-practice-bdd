from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.button import Button
from page_objects.choose_payment_method_page.choose_payment_method_page_locators import ChoosePaymentMethodPageLocators as Locators

class ChoosePaymentMethodPage(AbsBasePage):

    pay_by_bank_wire = Button(Locators.PAY_BY_BANK_WIRE)
    pay_by_check = Button(Locators.PAY_BY_CHECK)

    def is_page_displayed(self):
        return self.pay_by_bank_wire.is_displayed()

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(self.pay_by_bank_wire.locator)
