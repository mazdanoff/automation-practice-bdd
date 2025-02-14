import time
from datetime import datetime, timedelta
from typing import Tuple

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class AbsPageObject:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_element_located_present(self, locator: Tuple[str, str]):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return False

    def is_element_located_displayed(self, locator: Tuple[str, str]):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def wait_for_presence_of_element_located(self, locator: Tuple[str, str], timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator))
        except TimeoutException:
            pass

    def wait_for_visibility_of_element_located(self, locator: Tuple[str, str], timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator))
        except TimeoutException:
            pass

    def wait_for_text_to_be_present_in_element_located(self, locator: Tuple[str, str], text: str, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            pass

    @staticmethod
    def wait_until(condition, *args, **kwargs):
        timeout = kwargs.pop("timeout", None) or 5
        interval = kwargs.pop("interval", None) or 0.5

        start_time = datetime.now()
        end_time = start_time + timedelta(seconds=timeout)
        while True:
            condition_met = condition(*args, **kwargs)
            if condition_met:
                return
            if datetime.now() > end_time:
                break
            time.sleep(interval)
