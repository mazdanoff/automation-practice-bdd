from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.abstract.web_elements.button import Button
from page_objects.category_navigation_bar.category_navigation_bar_locators import CategoryNavigationBarLocators as Locators

class CategoryNavigationBar(AbsPageObject):

    women_button = Button(Locators.WOMEN_BUTTON)
