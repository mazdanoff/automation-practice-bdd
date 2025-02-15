from functools import partial

from hamcrest import assert_that, equal_to
from pytest_bdd import scenario, given, when, then, parsers
from selenium.webdriver.firefox.webdriver import WebDriver

from conf.paths import features_dir
from conf.urls import MAIN_PAGE_URL
from page_objects.choose_address_page.choose_address_page import ChooseAddressPage
from page_objects.category_navigation_bar.category_navigation_bar import CategoryNavigationBar
from page_objects.category_navigation_bar.women_submenu import WomenSubmenu
from page_objects.category_page.category_page import CategoryPage
from page_objects.choose_payment_method_page.choose_payment_method_page import ChoosePaymentMethodPage
from page_objects.choose_shipping_page.choose_shipping_page import ChooseShippingPage
from page_objects.login_or_register.login_or_register_page import LoginOrRegisterPage
from page_objects.main_page.main_page import MainPage
from page_objects.my_account.my_account_page import MyAccountPage
from page_objects.account_navigation_bar.account_navigation_bar_object import TopNavigationBarObject
from page_objects.order_confirmation_page.order_confirmation_page import OrderConfirmationPage
from page_objects.order_summary_page.order_summary_page import OrderSummaryPage
from page_objects.product_page.confirmation_banner import ConfirmationBanner
from page_objects.product_page.product_page import ProductPage
from page_objects.shopping_cary_summary.shopping_cart_summary_page import ShoppingCartSummaryPage

scenario = partial(scenario, f"{features_dir}/shopping_flow.feature")

CREDENTIALS = {
    "email_address": "mail@email.com",
    "password": "meant4",
}

ADDRESS_DETAILS = {
    "first_name": "Florence",
    "last_name": "Lawrence",
    "address": "Testing St.",
    "city": "Honolulu",
    "state": "Hawaii",
    "postal_code": "11337",
    "home_phone": "+48333222111",
    "mobile_phone": "+48111222333",
    "address_title": "My address",
}


@scenario("Basic flow")
def test_basic_flow(driver: WebDriver):
    pass

# @scenario("Using search")
# def test_using_search(driver: WebDriver):
#     pass
#
# @scenario("Using search hints")
# def test_using_search_hints(driver: WebDriver):
#     pass

@given("YourLogo main page is displayed")
def step_yourlogo_main_page_is_displayed(driver: WebDriver):
    main_page = MainPage(driver, MAIN_PAGE_URL).open()
    main_page.wait_for_page_to_load()
    assert_that(main_page.is_page_displayed(), "Main page is not displayed")

@given("I'm logged in")
def step_im_logged_in(driver: WebDriver):
    sign_in_button = TopNavigationBarObject(driver).sign_in
    assert_that(sign_in_button.is_displayed(), "'Sign in' button is not displayed")
    sign_in_button.click()

    login_or_register_page = LoginOrRegisterPage(driver)
    login_or_register_page.wait_for_page_to_load()
    assert_that(login_or_register_page.is_page_displayed(), "Login page is not displayed")
    login_or_register_page.already_registered.submit_form(CREDENTIALS)

    my_account_page = MyAccountPage(driver)
    my_account_page.wait_for_page_to_load()
    assert_that(my_account_page.is_page_displayed(), "'My Account' page is not displayed")

    main_page = MainPage(driver, MAIN_PAGE_URL).open()
    main_page.wait_for_page_to_load()
    assert_that(main_page.is_page_displayed(), "Main page is not displayed")

@when("I go to 'Tops' category")
def step_i_go_to_tops_category(driver: WebDriver):
    nav_bar = CategoryNavigationBar(driver)
    women_submenu = WomenSubmenu(driver)
    nav_bar.hover_over(nav_bar.women_button.element)
    women_submenu.wait_for_submenu_to_appear()
    assert_that(women_submenu.tops_link.is_displayed(), "The 'Women' submenu is not displayed")
    women_submenu.tops_link.click()

@when("I pick the 'Blouse' item")
def step_i_pick_the_blouse_item(driver: WebDriver):
    category_page = CategoryPage(driver)
    category_page.wait_for_page_to_load()
    assert_that(category_page.is_page_displayed(), "'Tops' category page is not displayed")
    picked_item = category_page.item_list.get_item_by_property(name='Blouse')
    assert_that(picked_item is not None, "Cannot find the expected 'Blouse' item")
    picked_item.name.click()
    ProductPage(driver).wait_for_page_to_load()

@when(parsers.parse("I choose size '{size}'"))
def step_i_choose_size(driver: WebDriver, size):
    ProductPage(driver).size.text = size

@when(parsers.parse("I choose {color_name} color"))
def step_i_choose_white_color(driver: WebDriver, color_name: str):
    color_name = color_name.capitalize()
    color = ProductPage(driver).color_picker.select_color_by_name(color_name)
    color.click()

@when(parsers.parse("I choose quantity of {quantity:d}"))
def step_i_choose_quantity_of_n(driver: WebDriver, quantity):
    ProductPage(driver).quantity.value = quantity

@when("I click 'Add to cart' button and proceed to checkout")
def step_i_click_add_to_cart_button_and_proceed_to_checkout(driver: WebDriver):
    ProductPage(driver).add_to_cart.click()

    confirmation_banner = ConfirmationBanner(driver)
    confirmation_banner.wait_for_banner_to_appear()
    confirmation_banner.proceed_to_checkout.click()

@when("I proceed to checkout on cart summary page")
def step_i_proceed_to_checkout_on_cart_summary_page(driver: WebDriver):
    cart_summary_page = ShoppingCartSummaryPage(driver)
    cart_summary_page.wait_for_page_to_load()
    cart_summary_page.proceed_to_checkout.click()

@when("I sign in")
def step_i_sign_in(driver: WebDriver):
    login_or_register_page = LoginOrRegisterPage(driver)
    login_or_register_page.wait_for_page_to_load()
    assert_that(login_or_register_page.is_page_displayed(), "FILL ME IN")
    login_or_register_page.already_registered.submit_form(CREDENTIALS)

@when("I choose my delivery address")
def step_i_choose_my_delivery_address(driver: WebDriver):
    address_page = ChooseAddressPage(driver)
    address_page.wait_for_page_to_load()
    assert_that(address_page.is_page_displayed(), "FILL ME IN")
    address_page.proceed_to_checkout.click()

@when("I choose shipping and agree to terms of service")
def step_i_agree_to_terms_of_service(driver: WebDriver):
    shipping_page = ChooseShippingPage(driver)
    shipping_page.wait_for_page_to_load()
    assert_that(shipping_page.is_page_displayed(), "FILL ME IN")
    shipping_page.terms_of_service.click()
    assert_that(shipping_page.terms_of_service.is_selected(), "FILL ME IN")
    shipping_page.proceed_to_checkout.click()

@when("I choose payment by bank-wire")
def step_i_choose_payment_by_bank_wire(driver: WebDriver):
    payment_method_page = ChoosePaymentMethodPage(driver)
    payment_method_page.wait_for_page_to_load()
    assert_that(payment_method_page.is_page_displayed(), "FILL ME IN")
    payment_method_page.pay_by_bank_wire.click()

@when("I confirm my order")
def step_i_confirm_my_order(driver: WebDriver):
    order_summary_page = OrderSummaryPage(driver)
    order_summary_page.wait_for_page_to_load()
    assert_that(order_summary_page.is_page_displayed(), "FILL ME IN")
    order_summary_page.confirm_order_button.click()

@when("I type 'summer' into the search bar")
def step_i_type_summer_into_the_search_bar(driver: WebDriver):
    pass

@when("I choose 'Tops' category")
def step_i_choose_tops_category(driver: WebDriver):
    pass

@when("I type 'Blouse' into the search bar")
def step_i_type_blouse_into_the_search_bar(driver: WebDriver):
    pass

@when("I choose the search bar's first hint")
def step_i_choose_the_search_bars_first_hint(driver: WebDriver):
    pass

@when("I click the search button")
def step_i_click_the_search_button(driver: WebDriver):
    pass

@when("I hover over 'WOMEN' category")
def step_i_hover_over_women_category(driver: WebDriver):
    pass

@then("the first item's name includes a 'Summer' word")
def step_the_first_items_name_includes_a_summer_word(driver: WebDriver):
    pass

@then("a 'Tops' category page is displayed")
def step_a_tops_category_page_is_displayed(driver: WebDriver):
    pass

@then("the product's name is 'Blouse'")
def step_the_products_name_is_blouse(driver: WebDriver):
    pass

@then("Order Confirmation page is displayed")
def step_order_confirmation_page_is_displayed(driver: WebDriver):
    order_confirmation_page = OrderConfirmationPage(driver)
    order_confirmation_page.wait_for_page_to_load(10)
    assert_that(order_confirmation_page.is_page_displayed(), "FILL ME IN")

@then(parsers.parse("a '{message}' message is displayed"))
def step_a_your_order_on_my_shop_is_complete_message_is_displayed(driver: WebDriver, message: str):
    alert = OrderConfirmationPage(driver).alert_notification.text
    assert_that(alert, equal_to(message))

@then("a product page is displayed")
def step_a_product_page_is_displayed(driver: WebDriver):
    pass

@then("the Search page is displayed")
def step_the_search_page_is_displayed(driver: WebDriver):
    pass

