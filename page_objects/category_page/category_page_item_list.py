from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class ItemList(DataTable):

    rows_locator = (By.CSS_SELECTOR, ".product_list > li")

    name = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) .right-block .product-name")
    price = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) .right-block span.product-price")
    availability = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) .right-block span.availability > span")
