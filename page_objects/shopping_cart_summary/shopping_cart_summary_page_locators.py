from selenium.webdriver.common.by import By


class ShoppingCartSummaryPageLocators:

    HEADER = (By.CLASS_NAME, "page-heading")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, ".cart_navigation a[title='Proceed to checkout'] > span")
    CART_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity_input")
    DECREASE_QUANTITY = (By.CSS_SELECTOR, "a.cart_quantity_down")
    INCREASE_QUANTITY = (By.CSS_SELECTOR, "a.cart_quantity_up")
    TOTAL_PRICE = (By.CSS_SELECTOR, "#total_price")
