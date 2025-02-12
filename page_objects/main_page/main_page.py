from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.abstract.web_elements.image import Image
from page_objects.main_page.main_page_locators import MainPageLocators as Locators

class MainPage(AbsBasePage):

    logo_image = Image(Locators.LOGO_IMG)

    def is_page_displayed(self):
        return self.logo_image.is_displayed()

    def wait_for_page_to_load(self, timeout: int = 5):
        self.wait_for_visibility_of_element_located(self.logo_image.locator)
