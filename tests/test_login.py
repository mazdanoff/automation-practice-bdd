import re
from functools import partial
from hamcrest import assert_that, equal_to
from pytest_bdd import scenario, given, when, then, parsers
from selenium.webdriver.firefox.webdriver import WebDriver

from conf.paths import features_dir
from conf.urls import MAIN_PAGE_URL, MY_ACCOUNT_PAGE_URL
from page_objects.login_or_register.already_registered_section_object import AlreadyRegisteredSection
from page_objects.login_or_register.login_or_register_page import LoginOrRegisterPage
from page_objects.my_account.my_account_page import MyAccountPage
from page_objects.main_page.main_page import MainPage
from page_objects.top_navigation_bar.top_navigation_bar_object import TopNavigationBarObject


scenario = partial(scenario, f"{features_dir}/login.feature")

CREDENTIALS = {
    "email_address": "mail@email.com",
    "password": "meant4",
}

@scenario("Happy Path")
def test_happy_path():
    pass

@scenario("Logging in using a wrong password for an existing user")
def test_logging_in_using_a_wrong_password_for_an_existing_user():
    pass

@scenario("A correct email format is highlighted in green")
def test_a_correct_email_format_is_highlighted_in_green():
    pass

@scenario("An incorrect email format is highlighted in red")
def test_an_incorrect_email_format_is_highlighted_in_red():
    pass

@scenario("A password with at least 5 characters is highlighted in green")
def test_a_password_with_at_least_five_characters_is_highlighted_in_green():
    pass

@scenario("A password with at most 4 characters is highlighted in red")
def test_a_password_with_at_most_four_characters_is_highlighted_in_red():
    pass

@scenario("An incorrect email format is not accepted by the Login page")
def test_an_incorrect_email_format_is_not_accepted_by_the_login_page():
    pass

@scenario("A too short password is not accepted by the Login page")
def test_a_too_short_password_is_not_accepted_by_the_login_page():
    pass

@scenario("Redirection of non-signed user to Login page")
def test_redirection_of_non_signed_user_to_login_page():
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

@when("I input my credentials in 'Already registered' section")
@when("I input credentials with correctly formatted email")
def step_i_input_my_credentials_in_already_registered_section(driver: WebDriver):
    login_section = LoginOrRegisterPage(driver).already_registered
    login_section.populate_form(CREDENTIALS)

@when("I click the green 'Sign in' button")
def step_i_click_the_green_sign_in_button(driver: WebDriver):
    LoginOrRegisterPage(driver).already_registered.sign_in.click()
    MyAccountPage(driver).wait_for_page_to_load()

@then("'My Account' page is displayed")
def step_my_account_page_is_displayed(driver: WebDriver):
    assert_that(MyAccountPage(driver).header.is_displayed(), "'My Account' page's header is not found")

@then("there's a 'Sign out' button in the top navigation bar")
def step_theres_a_sign_out_button_in_the_top_navigation_bar(driver: WebDriver):
    assert_that(TopNavigationBarObject(driver).sign_out.is_displayed(), "'Sign out' button is not displayed")

@then("my name is displayed in the top navigation bar")
def step_my_name_is_displayed_in_the_top_navigation_bar(driver: WebDriver):
    user_account_name = TopNavigationBarObject(driver).user_account_name
    assert_that(user_account_name.is_displayed(), "User's account name is not displayed")
    assert_that(user_account_name.text, equal_to("Romuald Mean"), "User's account name is not displayed")

@when("I attempt to open 'My Account' page by url")
def step_i_attempt_to_open_my_account_page_by_url(driver: WebDriver):
    driver.get(MY_ACCOUNT_PAGE_URL)

@then("Login page is displayed")
def step_login_page_is_displayed(driver: WebDriver):
    login_or_register_page = LoginOrRegisterPage(driver)
    login_or_register_page.wait_for_page_to_load()
    assert_that(login_or_register_page.is_page_displayed(), "Login page is not displayed")

@then("My Account page is not displayed")
def step_my_account_page_is_not_displayed(driver: WebDriver):
    assert_that(MyAccountPage(driver).is_page_displayed(), equal_to(False),
                "My Account page is displayed, but it should not")

@given("Already Registered section is displayed")
def step_already_registered_section_is_displayed(driver: WebDriver):
    assert_that(AlreadyRegisteredSection(driver).sign_in.is_displayed(), "Already Registered section is not displayed")

@then("the email address field is highlighted in green")
def step_the_email_address_field_is_highlighted_in_green(driver: WebDriver):
    email_address_field = AlreadyRegisteredSection(driver).email_address
    actual_color = email_address_field.element.value_of_css_property("color")
    assert_that(actual_color, equal_to("rgb(53, 179, 63)"))  #35b33f

@then("the password field is highlighted in green")
def step_the_password_field_is_highlighted_in_green(driver: WebDriver):
    password_field = AlreadyRegisteredSection(driver).password
    actual_color = password_field.element.value_of_css_property("color")
    assert_that(actual_color, equal_to("rgb(53, 179, 63)"))  #35b33f

@then("the email address field is highlighted in red")
def step_the_email_address_field_is_highlighted_in_red(driver: WebDriver):
    email_address_field = AlreadyRegisteredSection(driver).email_address
    actual_color = email_address_field.element.value_of_css_property("color")
    assert_that(actual_color, equal_to("rgb(241, 51, 64)"))  #f13340

@then("the password field is highlighted in red")
def step_the_password_field_is_highlighted_in_red(driver: WebDriver):
    password_field = AlreadyRegisteredSection(driver).password
    actual_color = password_field.element.value_of_css_property("color")
    assert_that(actual_color, equal_to("rgb(241, 51, 64)"))  #f13340

@then("an OK icon is displayed in the email address field")
def step_an_ok_icon_is_displayed_in_the_email_address_field(driver: WebDriver):
    email_address_field = AlreadyRegisteredSection(driver).email_address
    icon_properties = email_address_field.element.value_of_css_property("background")
    actual_icon_url = re.search(r'url\(\"(.*)\"', icon_properties).group(1) or ""
    assert_that(actual_icon_url, equal_to("../img/icon/form-ok.png"),
                f"The displayed icon is not OK, but \"{actual_icon_url}\"")

@then("an X icon is displayed in the email address field")
def step_an_x_icon_is_displayed_in_the_email_address_field(driver: WebDriver):
    email_address_field = AlreadyRegisteredSection(driver).email_address
    icon_properties = email_address_field.element.value_of_css_property("background")
    actual_icon_url = re.search(r'url\(\"(.*)\"', icon_properties).group(1) or ""
    assert_that(actual_icon_url, equal_to("../img/icon/form-error.png"),
                f"The displayed icon is not OK, but \"{actual_icon_url}\"")

@then("an OK icon is displayed in the password field")
def step_an_ok_icon_is_displayed_in_the_password_field(driver: WebDriver):
    password_field = AlreadyRegisteredSection(driver).password
    icon_properties = password_field.element.value_of_css_property("background")
    actual_icon_url = re.search(r'url\(\"(.*)\"', icon_properties).group(1) or ""
    assert_that(actual_icon_url, equal_to("../img/icon/form-ok.png"),
                f"The displayed icon is not OK, but \"{actual_icon_url}\"")

@then("an X icon is displayed in the password field")
def step_an_x_icon_is_displayed_in_the_password_field(driver: WebDriver):
    password_field = AlreadyRegisteredSection(driver).password
    icon_properties = password_field.element.value_of_css_property("background")
    actual_icon_url = re.search(r'url\(\"(.*)\"', icon_properties).group(1) or ""
    assert_that(actual_icon_url, equal_to("../img/icon/form-error.png"),
                f"The displayed icon is not OK, but \"{actual_icon_url}\"")

@when("I input credentials with incorrectly formatted email")
def step_i_input_credentials_with_incorrectly_formatted_email(driver: WebDriver):
    credentials = {
        "email_address": "clearly@lacking",
        "password": "meant4",
    }
    login_section = LoginOrRegisterPage(driver).already_registered
    login_section.populate_form(credentials)

@when("I input credentials with a wrong password")
def step_i_input_credentials_with_a_wrong_password(driver: WebDriver):
    credentials = {
        "email_address": CREDENTIALS["email_address"],
        "password": "crapicantremembermypassworditsprobablymisstyped",
    }
    login_section = LoginOrRegisterPage(driver).already_registered
    login_section.populate_form(credentials)

@then(parsers.parse("an '{expected_alert}' alert is displayed"))
def step_an_expected_alert_is_displayed(driver: WebDriver, expected_alert: str):
    alert = LoginOrRegisterPage(driver).alert_notification
    assert_that(alert.is_displayed(), "No alert is displayed")
    assert_that(alert.text, equal_to(expected_alert), f"A different alert is shown: {alert.text}")

@when(parsers.parse("I input credentials with password of length of {n:d}"))
def step_i_input_credentials_with_password_of_length_of_n(driver: WebDriver, n):
    credentials = {
        "password": "1"*n,
        "email_address": CREDENTIALS["email_address"],
    }  # writing fields in reverse order to click away from password field and trigger the background/color change
    login_section = LoginOrRegisterPage(driver).already_registered
    login_section.populate_form(credentials)
