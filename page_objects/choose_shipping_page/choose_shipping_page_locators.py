from selenium.webdriver.common.by import By


class ChooseShippingPageLocators:

    HEADER = (By.CLASS_NAME, "page-heading")
    TERMS_OF_SERVICES = (By.CSS_SELECTOR, "#uniform-cgv input")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "button[name='processCarrier'] > span")
    NOTIFICATION_POPUP = (By.CLASS_NAME, "fancybox-error")
