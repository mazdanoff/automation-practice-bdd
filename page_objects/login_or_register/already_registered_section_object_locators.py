from selenium.webdriver.common.by import By


class AlreadyRegisteredObjectLocators:

    EMAIL_FIELD = (By.ID, "email")
    PASSWD_FIELD = (By.ID, "passwd")
    SIGN_IN = (By.ID, "SubmitLogin")
