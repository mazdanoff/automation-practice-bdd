from selenium.webdriver.common.by import By
from selenium_datatable import Column

from page_objects.category_page.filters.category_page_filter import CategoryPageFilter


class FilterSize(CategoryPageFilter):

    rows_locator = (By.CLASS_NAME, "nomargin")

    name = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) label > a")
    amount_preview = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) label > a > span")
    checkbox = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) .checker")
