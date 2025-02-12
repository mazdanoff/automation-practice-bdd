from page_objects.abstract.web_elements.element import Element


class Button(Element):

    def click(self):
        self.element.click()

    @property
    def text(self):
        return self.element.text
