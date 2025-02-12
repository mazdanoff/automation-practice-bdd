from page_objects.abstract.web_elements.element import Element


class Text(Element):

    @property
    def text(self):
        return self.element.text
