from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.link import Link
from page_objects.category_navigation_bar.category_navigation_bar_locators import CategoryNavigationBarLocators as Locators

class WomenSubmenu(AbsPageObject):

    tops_link = Link(Locators.TOPS_LINK)

    def wait_for_submenu_to_appear(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(Locators.TOPS_LINK, timeout=timeout)
