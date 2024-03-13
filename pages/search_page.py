from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import SearchLocator


class SearchPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.locator = SearchLocator
        super().__init__(driver)

    def type_on_search_field(self, search_item):
        self.find_element(*self.locator.SEARCH_INPUT_FIELD).click()
        self.find_element(*self.locator.SEARCH_INPUT_FIELD).send_keys(search_item, Keys.ENTER)

