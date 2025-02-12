from selenium.webdriver.common.by import By


class LoginOrRegisterPageLocators:

    HEADER = (By.CLASS_NAME, "page-heading")
    ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#center_column > .alert ol")
