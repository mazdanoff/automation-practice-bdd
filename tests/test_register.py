import re
from functools import partial

from hamcrest import assert_that, equal_to
from pytest_bdd import scenario, given, when, then
from selenium.webdriver.firefox.webdriver import WebDriver

from conf.paths import features_dir
from conf.urls import MAIN_PAGE_URL
from page_objects.login_or_register.create_an_account_section_object import CreateAnAccountSection
from page_objects.login_or_register.login_or_register_page import LoginOrRegisterPage
from page_objects.main_page.main_page import MainPage
from page_objects.top_navigation_bar.top_navigation_bar_object import TopNavigationBarObject


scenario = partial(scenario, f"{features_dir}/register.feature")

CREDENTIALS = {
    "email_address": "mail@email.com",
}

# @scenario("Main Page display")
# def test_happy_path():
#     # potential for teardown to remove the account
#     # created for the purpose of this test case
#     # to keep the test environment clean

@scenario("A correct email format is highlighted in green")
def test_a_correct_email_format_is_highlighted_in_green():
    pass

# @scenario("Registering an existing account on 'Authentication' page is rejected")
# def test_registering_an_existing_account_on_authentication_page_is_rejected():
#     pass

@given("YourLogo main page is displayed")
def step_yourlogo_main_page_is_displayed(driver: WebDriver):
    main_page = MainPage(driver, MAIN_PAGE_URL).open()
    main_page.wait_for_page_to_load()
    assert_that(main_page.is_page_displayed(), "Main page is not displayed")

@given("there's a 'Sign in' button in top navigation bar")
@then("there's a 'Sign in' button in top navigation bar")
def step_theres_a_sign_in_button_in_top_navigation_bar(driver: WebDriver):
    sign_in_button = TopNavigationBarObject(driver).sign_in
    assert_that(sign_in_button.is_displayed(), "'Sign in' button is not displayed")

@given("I click a 'Sign in' button in the top navigation bar")
@when("I click a 'Sign in' button in the top navigation bar")
def step_i_click_a_sign_in_button_in_the_top_navigation_bar(driver: WebDriver):
    TopNavigationBarObject(driver).sign_in.click()
    LoginOrRegisterPage(driver).wait_for_page_to_load()

@when("I input my email address in 'Create an account' section")
def step_i_input_my_email_address_in_create_an_account_section(driver: WebDriver):
    login_or_register_page = LoginOrRegisterPage(driver)
    login_or_register_page.create_an_account.populate_form(CREDENTIALS)

    # the cursor stays in the email field
    # the field won't update its background/color until we click away from it to defocus
    login_or_register_page.header.element.click()

@then("the email address field is highlighted in green")
def step_the_email_address_field_is_highlighted_in_green(driver: WebDriver):
    email_address_field = CreateAnAccountSection(driver).email_address
    actual_color = email_address_field.element.value_of_css_property("color")
    assert_that(actual_color, equal_to("rgb(53, 179, 63)"))  # 35b33f

@then("an OK icon is displayed in the email address field")
def step_an_ok_icon_is_displayed_in_the_email_address_field(driver: WebDriver):
    email_address_field = CreateAnAccountSection(driver).email_address
    icon_properties = email_address_field.element.value_of_css_property("background")
    actual_icon_url = re.search(r'url\(\"(.*)\"', icon_properties).group(1) or ""
    assert_that(actual_icon_url, equal_to("../img/icon/form-ok.png"),
                f"The displayed icon is not OK, but \"{actual_icon_url}\"")
