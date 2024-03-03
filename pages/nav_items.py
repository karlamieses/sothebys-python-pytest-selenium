from utils.locators import LogOutLocator
from pages.base_page import BasePage


class NavigationItems(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.locator = LogOutLocator
        super().__init__(driver)

    def click_logout_button(self):
        self.driver.find_element(*self.locator.LOGOUT_BUTTON).click()
