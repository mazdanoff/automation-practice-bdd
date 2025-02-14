from functools import partial

from hamcrest import assert_that, equal_to
from pytest_bdd import scenario, parsers, given, when, then
from selenium.webdriver.firefox.webdriver import WebDriver

from conf.paths import features_dir
from conf.urls import WOMEN_CATEGORY_URL
from page_objects.category_page.category_page import CategoryPage

scenario = partial(scenario, f"{features_dir}/item_sort_filter.feature")

@scenario("Item filtering")
def test_item_filtering():
    pass


@given("'WOMEN' category page is displayed")
def step_women_category_page_is_displayed(driver: WebDriver):
    category_page = CategoryPage(driver, WOMEN_CATEGORY_URL).open()
    category_page.wait_for_page_to_load()
    assert_that(category_page.is_page_displayed(), "'WOMEN' category page is not displayed")

@given(parsers.parse("there are {expected_amount:d} items available"))
@then(parsers.parse("there are {expected_amount:d} items available"))
def step_there_are_x_items_available(driver: WebDriver, expected_amount):
    actual_amount = len(CategoryPage(driver).item_list)
    assert_that(actual_amount, equal_to(expected_amount),
                f"Item amount mismatch: expected {expected_amount}, but is {actual_amount}")

@when(parsers.parse("I filter by '{option}' in '{filter_name}'"))
def step_i_filter_by(driver: WebDriver, option, filter_name):
    category_page = CategoryPage(driver)
    filters = {
        "Categories": category_page.categories_filter,
        "Size": category_page.size_filter,
        "Color": category_page.color_filter,
        "Availability": category_page.availability_filter,
    }
    current_filter = filters[filter_name]  # i.e. Size filters
    option = current_filter.get_by_name(name=option)  # i.e. 'L' size in Size filters
    amount_preview = current_filter.get_amount(option.amount_preview.text)
    option.checkbox.click()
    category_page.wait_until_item_count_matches(expected_amount=amount_preview)
