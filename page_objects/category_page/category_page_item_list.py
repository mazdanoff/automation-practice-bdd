from selenium.webdriver.common.by import By
from selenium_datatable import DataTable


class ItemList(DataTable):

    rows_locator = (By.CLASS_NAME, "product-container")

    image = (By.CLASS_NAME, "img-responsive")
    name = (By.CLASS_NAME, "product-name")
    availability = (By.CSS_SELECTOR, "span.availability > span")
