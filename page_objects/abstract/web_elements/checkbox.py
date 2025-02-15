from page_objects.abstract.web_elements.element import Element


class Checkbox(Element):

    def click(self):
        self.element.click()

    def is_selected(self):
        return self.element.is_selected()
