from selenium.webdriver.common.by import By


class SearchPageLocators:

    HEADER = (By.CSS_SELECTOR, ".page-heading.product-listing")
    ITEM_LIST = (By.CLASS_NAME, "product_list")
