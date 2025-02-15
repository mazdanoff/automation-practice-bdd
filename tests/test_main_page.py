from hamcrest import assert_that
from pytest_bdd import scenario, given, when, then
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.by import By

from conf.paths import features_dir
from conf.urls import MAIN_PAGE_URL

@scenario(f"{features_dir}/main_page.feature", "Main Page display")
def test_main_page_display():
    pass

@given("I open the browser")
def open_browser(driver: WebDriver):
    assert driver

@when("I open the url 'http://www.automationpractice.pl'")
def open_main_page_url(driver: WebDriver):
    driver.get(MAIN_PAGE_URL)

@then("the YourLogo shop's main page is displayed")
def main_page_is_displayed(driver):
    header_logo_locator = (By.ID, "header_logo")
    wait(driver, 5).until(
        EC.visibility_of_element_located(header_logo_locator)
    )
    assert_that(driver.find_element(*header_logo_locator).is_displayed())
