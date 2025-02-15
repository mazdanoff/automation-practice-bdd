from selenium.webdriver.common.by import By


class ProductPageLocators:

    # righthand menu
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    QUANTITY = (By.ID, "quantity_wanted")
    SIZE = (By.ID, "group_1")
    COLOR_LIST = (By.ID, "color_to_pick_list")
    COLOR_SINGLE = (By.CLASS_NAME, "color_pick")
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_cart > button")

    # confirmation banner
    CONFIRMATION_BANNER = (By.ID, "layer_cart")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "a[title='Proceed to checkout'] > span")
