from selenium.webdriver.common.by import By


class CategoryPageLocators:

    ITEM_LIST = (By.CLASS_NAME, "product_list")
    FILTER_CATEGORIES = (By.ID, "ul_layered_category_0")
    FILTER_SIZE = (By.ID, "ul_layered_id_attribute_group_1")
    FILTER_COLOR = (By.ID, "ul_layered_id_attribute_group_3")
    FILTER_AVAILABILITY = (By.ID, "ul_layered_quantity_0")
