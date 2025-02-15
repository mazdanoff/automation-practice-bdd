from selenium.webdriver.common.by import By


class ShoppingCartSummaryPageLocators:

    HEADER = (By.CLASS_NAME, "page-heading")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, ".cart_navigation a[title='Proceed to checkout'] > span")
