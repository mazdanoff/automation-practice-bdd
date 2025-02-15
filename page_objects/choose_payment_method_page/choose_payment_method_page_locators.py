from selenium.webdriver.common.by import By


class ChoosePaymentMethodPageLocators:

    PAY_BY_BANK_WIRE = (By.CLASS_NAME, "bankwire")
    PAY_BY_CHECK = (By.CLASS_NAME, "cheque")
