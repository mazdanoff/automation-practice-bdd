from selenium.webdriver.remote.webelement import WebElement

from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.abstract.web_elements.button import Button
from page_objects.abstract.web_elements.input_field import InputField
from page_objects.search_bar.search_bar_locators import SearchBarLocators as Locators


class HintListRangeException(KeyError):
    pass

class SearchBar(AbsPageObject):

    field = InputField(Locators.FIELD)
    submit = Button(Locators.SUBMIT)

    def __init__(self, driver):
        super().__init__(driver)
        self.hint_list = HintList(driver)

class HintList(AbsPageObject):

    def wait_for_hints_to_appear(self):
        self.wait_for_visibility_of_element_located(Locators.HINT_LIST)

    def is_displayed(self):
        return self.is_element_located_displayed(Locators.HINT_LIST)

    def get_hint_by_text(self, text) -> WebElement:
        for hint in self._hints:
            if hint.text == text:
                return hint

    def __getitem__(self, index: int) -> WebElement:
        len_ = len(self)
        if index < 0:
            index += len_
        for i, hint in enumerate(self._hints):
            if i == index:
                return hint
        raise HintListRangeException("Hint out of range")

    def __len__(self):
        return len(self._hints)

    @property
    def _hints(self) -> list[WebElement]:
        hint_list = self.driver.find_element(*Locators.HINT_LIST)
        hints = hint_list.find_elements(*Locators.HINT_SINGLE)
        return hints
