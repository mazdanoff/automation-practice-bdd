import re
from functools import partial

from hamcrest import assert_that, equal_to
from pytest_bdd import scenario, given, when, then, parsers
from selenium.webdriver.firefox.webdriver import WebDriver

from conf.paths import features_dir
from conf.urls import MAIN_PAGE_URL
from page_objects.create_an_account.create_an_account_page import CreateAnAccountPage
from page_objects.login_or_register.create_an_account_section_object import CreateAnAccountSection
from page_objects.login_or_register.login_or_register_page import LoginOrRegisterPage
from page_objects.main_page.main_page import MainPage
from page_objects.my_account.my_account_page import MyAccountPage
from page_objects.account_navigation_bar.account_navigation_bar_object import TopNavigationBarObject


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

@scenario("An incorrect email format is highlighted in red")
def test_an_incorrect_email_format_is_highlighted_in_red():
    pass

@scenario("Registering an existing account on 'Authentication' page is rejected")
def test_registering_an_existing_account_on_authentication_page_is_rejected():
    pass

@scenario("Registering an existing account on 'Create an account' page is rejected")
def test_registering_an_existing_account_on_create_an_account_page_is_rejected():
    pass

@scenario("Registering using an incorrectly formatted email is rejected")
def test_registering_using_an_incorrectly_formatted_email_is_rejected():
    pass

@scenario("Registering while leaving a required field empty is rejected")
def test_registering_while_leaving_a_required_field_empty_is_rejected():
    pass

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
@when("I input an email address for an existing account in 'Create an account' section")
def step_i_input_my_email_address_in_create_an_account_section(driver: WebDriver):
    login_or_register_page = LoginOrRegisterPage(driver)
    login_or_register_page.create_an_account.populate_form(CREDENTIALS)

    # the cursor stays in the email field
    # the field won't update its background/color until we click away from it to defocus
    login_or_register_page.header.element.click()

@when("I input an incorrectly formatted email in 'Create an account' section")
def step_i_input_an_incorrectly_formatted_email_in_create_an_account_section(driver: WebDriver):
    credentials = {
        "email_address": "purposefully@wrong"
    }
    login_or_register_page = LoginOrRegisterPage(driver)
    login_or_register_page.create_an_account.populate_form(credentials)

    # the cursor stays in the email field
    # the field won't update its background/color until we click away from it to defocus
    login_or_register_page.header.element.click()

@then("the email address field is highlighted in green")
def step_the_email_address_field_is_highlighted_in_green(driver: WebDriver):
    email_address_field = CreateAnAccountSection(driver).email_address
    actual_color = email_address_field.element.value_of_css_property("color")
    assert_that(actual_color, equal_to("rgb(53, 179, 63)"))  #35b33f

@then("an OK icon is displayed in the email address field")
def step_an_ok_icon_is_displayed_in_the_email_address_field(driver: WebDriver):
    email_address_field = CreateAnAccountSection(driver).email_address
    icon_properties = email_address_field.element.value_of_css_property("background")
    actual_icon_url = re.search(r'url\(\"(.*)\"', icon_properties).group(1) or ""
    assert_that(actual_icon_url, equal_to("../img/icon/form-ok.png"),
                f"The displayed icon is not OK, but \"{actual_icon_url}\"")

@then("the email address field is highlighted in red")
def step_the_email_address_field_is_highlighted_in_red(driver: WebDriver):
    email_address_field = CreateAnAccountSection(driver).email_address
    actual_color = email_address_field.element.value_of_css_property("color")
    assert_that(actual_color, equal_to("rgb(241, 51, 64)"))  #f13340

@then("an X icon is displayed in the email address field")
def step_an_x_icon_is_displayed_in_the_email_address_field(driver: WebDriver):
    email_address_field = CreateAnAccountSection(driver).email_address
    icon_properties = email_address_field.element.value_of_css_property("background")
    actual_icon_url = re.search(r'url\(\"(.*)\"', icon_properties).group(1) or ""
    assert_that(actual_icon_url, equal_to("../img/icon/form-error.png"),
                f"The displayed icon is not OK, but \"{actual_icon_url}\"")

@when("I click a yellow 'Create an account' button")
def step_i_click_a_yellow_create_an_account_button(driver: WebDriver):
    CreateAnAccountSection(driver).create_an_account.click()

@then(parsers.parse("I get an '{message}' alert in 'Create an account' section on Authentication page"))
def step_i_get_an_message_alert_in_create_an_account_section_on_authentication_page(driver: WebDriver, message: str):
    alert_notification = CreateAnAccountSection(driver).alert_notification
    assert_that(alert_notification.is_displayed(), "No alert to be found")
    assert_that(alert_notification.text, equal_to(message),
                f"Retrieved message differs from expected: '{message}'")

@then("'Create an account' page is not displayed")
def step_create_an_account_page_is_not_displayed(driver: WebDriver):
    assert_that(CreateAnAccountPage(driver).is_page_displayed(), equal_to(False),
                "Create an account page is displayed")

@when("I input an email address for a non-existing account in 'Create an account' section")
def step_i_input_an_email_address_for_a_non_existing_account_in_create_an_account_section(driver: WebDriver):
    credentials = {
        "email_address": "iDoNot@Exist.yet"
    }
    login_or_register_page = LoginOrRegisterPage(driver)
    login_or_register_page.create_an_account.populate_form(credentials)

    # the cursor stays in the email field
    # the field won't update its background/color until we click away from it to defocus
    login_or_register_page.header.element.click()

@when("I submit the form on 'Create an account' page using an email address for an existing account")
def step_i_submit_the_form_on_create_an_account_page_using_an_email_address_for_an_existing_account(driver: WebDriver):
    create_an_account_page = CreateAnAccountPage(driver)
    credentials = {
        "first_name": "Florence",
        "last_name": "Lawrence",
        "email_address": "mail@email.com",  # taken by Romuald Mean
        "password": "lorenz",
        "birth_day": "31",
        "birth_month": "12",
        "birth_year": "1969",
    }
    create_an_account_page.wait_for_page_to_load()
    create_an_account_page.submit_form(credentials)

@when("I submit the form on 'Create an account' page using an incorrectly formatted email address")
def step_i_submit_the_form_on_create_an_account_page_using_an_incorrectly_formatted_email_address(driver: WebDriver):
    create_an_account_page = CreateAnAccountPage(driver)
    credentials = {
        "first_name": "Florence",
        "last_name": "Lawrence",
        "email_address": "purposefully@wrong",
        "password": "lorenz",
        "birth_day": "31",
        "birth_month": "12",
        "birth_year": "1969",
    }
    create_an_account_page.wait_for_page_to_load()
    create_an_account_page.submit_form(credentials)

@when("I submit the form on 'Create an account' page while omitting the required password field")
def step_i_submit_the_form_on_create_an_account_page_while_omitting_the_required_password_field(driver: WebDriver):
    create_an_account_page = CreateAnAccountPage(driver)
    credentials = {
        "first_name": "Florence",
        "last_name": "Lawrence",
        "email_address": "itscorrect@this.time",
        "birth_day": "31",
        "birth_month": "12",
        "birth_year": "1969",
    }
    create_an_account_page.wait_for_page_to_load()
    create_an_account_page.submit_form(credentials)

@then(parsers.parse("I get an '{message}' alert on 'Create an account' page"))
def step_i_get_an_message_alert_on_create_an_account_page(driver: WebDriver, message):
    alert_notification = CreateAnAccountPage(driver).alert_notification
    assert_that(alert_notification.is_displayed(), "No alert is displayed")
    assert_that(alert_notification.text, equal_to(message),
                f"Received alert message is different: {alert_notification.text}")

@then("'My Account' page is not displayed")
def step_my_account_page_is_not_displayed(driver: WebDriver):
    assert_that(MyAccountPage(driver).is_page_displayed(), equal_to(False),
                "'My Account' page is displayed either way")
