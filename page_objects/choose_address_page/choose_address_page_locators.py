from selenium.webdriver.common.by import By


class ChooseAddressPageLocators:

    HEADER = (By.CLASS_NAME, "page-heading")
    MY_ADDRESS = (By.ID, "id_address_delivery")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "button[name='processAddress'] > span")
