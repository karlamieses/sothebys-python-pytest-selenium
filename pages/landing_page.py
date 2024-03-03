from pages.base_page import BasePage
from utils.locators import MainPageLocator


class LandingPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = MainPageLocator
        super().__init__(driver)

    def click_login_button(self):
        self.find_element(*self.locator.LOGIN_BUTTON).click()



