from selenium.webdriver.common.by import By


class CreateAnAccountObjectLocators:

    EMAIL_FIELD = (By.ID, "email_create")
    CREATE_AN_ACCOUNT = (By.ID, "SubmitCreate")
    ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#create_account_error li")
