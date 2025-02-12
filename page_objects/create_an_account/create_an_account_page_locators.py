from selenium.webdriver.common.by import By


class CreateAnAccountPageLocators:

    HEADER = (By.CLASS_NAME, "page-heading")
    FIRST_NAME = None
    LAST_NAME = None
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD = None
    BIRTH_DAY = None
    BIRTH_MONTH = None
    BIRTH_YEAR = None
    REGISTER = (By.ID, "submitAccount")

