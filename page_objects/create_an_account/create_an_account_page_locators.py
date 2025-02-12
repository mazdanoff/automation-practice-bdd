from selenium.webdriver.common.by import By


class CreateAnAccountPageLocators:

    HEADER = (By.CLASS_NAME, "page-heading")
    MR_TITLE = (By.ID, "id_gender1")
    MRS_TITLE = (By.ID, "id_gender2")
    FIRST_NAME = (By.ID, "customer_firstname")
    LAST_NAME = (By.ID, "customer_lastname")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    BIRTH_DAY = (By.CSS_SELECTOR, "select#days")
    BIRTH_MONTH = (By.CSS_SELECTOR, "select#months")
    BIRTH_YEAR = (By.CSS_SELECTOR, "select#years")
    REGISTER = (By.ID, "submitAccount")
    ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#center_column > .alert ol")

