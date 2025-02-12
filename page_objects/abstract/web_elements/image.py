from page_objects.abstract.web_elements.element import Element


class Image(Element):

    @property
    def img_src(self):
        return self.element.get_attribute("src")
