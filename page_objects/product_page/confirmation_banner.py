from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.abstract.web_elements.button import Button
from page_objects.product_page.product_page_locators import ProductPageLocators as Locators

class ConfirmationBanner(AbsPageObject):

    proceed_to_checkout = Button(Locators.PROCEED_TO_CHECKOUT)

    def wait_for_banner_to_appear(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(Locators.PROCEED_TO_CHECKOUT, timeout=timeout)
