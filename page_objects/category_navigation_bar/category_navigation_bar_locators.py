from selenium.webdriver.common.by import By


class CategoryNavigationBarLocators:

    WOMEN_BUTTON = (By.CSS_SELECTOR, "#block_top_menu a[title='Women']")

    TOPS_LINK = (By.CSS_SELECTOR, "#block_top_menu li:nth-of-type(1) a[title='Tops']")
