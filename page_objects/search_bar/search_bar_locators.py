from selenium.webdriver.common.by import By


class SearchBarLocators:

    FIELD = (By.ID, "search_query_top")
    SUBMIT = (By.CLASS_NAME, "button-search")
    HINT_LIST = (By.CLASS_NAME, "ac_results")
    HINT_SINGLE = (By.TAG_NAME, "li")
