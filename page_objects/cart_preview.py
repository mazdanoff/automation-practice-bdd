from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.text import Text
from page_objects.cart_preview_locators import CartPreviewLocators as Locators

class CartPreview(AbsPageObject):

    cart = Button(Locators.CART)
    product_name = Text(Locators.PRODUCT_NAME)
    product_qty = Text(Locators.PRODUCT_QTY)

    def hover_over_cart(self):
        self.hover_over(to_element=self.cart.element)

    def wait_for_cart_details_to_display(self):
        self.wait_for_visibility_of_element_located(Locators.CHECKOUT, timeout=5)

    def is_displayed(self):
        return self.is_element_located_displayed(Locators.CHECKOUT)
