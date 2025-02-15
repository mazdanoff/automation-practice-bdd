from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.dropdown import Dropdown
from page_objects.abstract.web_elements.input_field import InputField
from page_objects.product_page.color_picker import ColorPicker
from page_objects.product_page.product_page_locators import ProductPageLocators as Locators

class ProductPage(AbsBasePage):

    size = Dropdown(Locators.SIZE)
    quantity = InputField(Locators.QUANTITY, wait_con=visibility_of_element_located)
    add_to_cart = Button(Locators.ADD_TO_CART, wait_con=visibility_of_element_located)

    def __init__(self, driver, url: str = None):
        super(ProductPage, self).__init__(driver, url)
        self.color_picker = ColorPicker(driver)

    def is_page_displayed(self):
        return self.size.is_displayed()

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(self.size.locator)
