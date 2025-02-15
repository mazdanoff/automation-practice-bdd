from selenium.webdriver.remote.webelement import WebElement

from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.product_page.product_page_locators import ProductPageLocators as Locators


class ColorNotFoundException(Exception):
    pass

class ColorPicker(AbsPageObject):

    def select_color_by_name(self, name: str) -> WebElement:
        color_list = self._get_color_list()
        for element in color_list:
            if name == element.get_attribute("name"):
                return element
        raise ColorNotFoundException(f"{name} color not present in {self.get_colors()}")

    def get_colors(self) -> list:
        colors = []
        color_list = self._get_color_list()
        for element in color_list:
            colors.append(element.get_attribute("name"))
        return colors

    def _get_color_list(self):
        color_picker = self.driver.find_element(*Locators.COLOR_LIST)
        return color_picker.find_elements(*Locators.COLOR_SINGLE)
