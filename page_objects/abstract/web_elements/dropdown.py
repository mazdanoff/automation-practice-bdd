from selenium.webdriver.support.select import Select

from page_objects.abstract.web_elements.element import Element


class Dropdown(Element):

    @property
    def value(self):
        select = Select(self.element)
        return select.first_selected_option.get_attribute("value")

    @value.setter
    def value(self, value):
        select = Select(self.element)
        select.select_by_value(value)

    @property
    def text(self):
        select = Select(self.element)
        return select.first_selected_option.text

    @text.setter
    def text(self, value):
        select = Select(self.element)
        select.select_by_visible_text(value)
