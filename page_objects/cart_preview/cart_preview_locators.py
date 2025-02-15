from selenium.webdriver.common.by import By


class CartPreviewLocators:

    CART = (By.CSS_SELECTOR, ".shopping_cart > a")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".cart_block_list .cart_block_product_name")
    PRODUCT_QTY = (By.CSS_SELECTOR, ".cart_block_list .quantity")
    CHECKOUT = (By.CSS_SELECTOR, "a#button_order_cart")
