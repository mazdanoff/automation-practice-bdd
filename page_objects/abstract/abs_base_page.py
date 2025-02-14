from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.abstract.abs_page_object import AbsPageObject


class UrlException(Exception):
    pass


class AbsBasePage(AbsPageObject, ABC):
    def __init__(self, driver: WebDriver, url: str = None):
        super(AbsBasePage, self).__init__(driver)
        self.url = url

    def open(self, url: str = None):
        url = url or self.url
        if not url:
            raise UrlException("URL not provided")
        self.driver.get(url)
        return self

    @abstractmethod
    def is_page_displayed(self):
        pass

    @abstractmethod
    def wait_for_page_to_load(self, timeout: int = 5):
        pass
