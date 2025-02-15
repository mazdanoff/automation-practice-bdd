from page_objects.abstract.abs_page_object import AbsPageObject
from page_objects.abstract.web_elements.button import Button
from page_objects.account_navigation_bar.account_navigation_bar_object_locators import TopNavigationBarObjectLocators as Locators


class TopNavigationBarObject(AbsPageObject):

    sign_in = Button(Locators.SIGN_IN)
    sign_out = Button(Locators.SIGN_OUT)
    user_account_name = Button(Locators.USER_ACCOUNT_NAME)
