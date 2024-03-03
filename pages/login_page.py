from pages.base_page import BasePage
from utils.locators import LoginPageLocator, SignUpPageLocator


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocator
        super().__init__(driver)

    def click_signup_button(self):
        self.find_element(*self.locator.SIGN_UP).click()


