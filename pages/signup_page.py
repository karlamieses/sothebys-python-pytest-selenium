from pages.base_page import BasePage
from utils.locators import SignUpPageLocator
from utils.users import get_user


class SignupPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = SignUpPageLocator
        super().__init__(driver)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_terms_and_conditions(self):
        self.find_element(*self.locator.TERMS_CHECK).click()

    def enter_first_name(self, first_name):
        self.find_element(*self.locator.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find_element(*self.locator.LAST_NAME).send_keys(last_name)


    def select_title(self):
        self.find_element(*self.locator.TITLE_LABEL).click()
        self.find_element(*self.locator.TITLE_LABEL_OPTION_MISS).click()

    def click_on_signup_button(self):
        self.find_element(*self.locator.SIGN_UP_BUTTON).click()

    def sign_up(self, user_name):
        user = get_user(user_name)
        print(user)
        self.enter_email(user["email"])
        self.enter_password(user["password"])
        self.enter_first_name(["first_name"])
        self.enter_last_name(user["last_name"])
        # self.select_title()
        # self.click_terms_and_conditions()
        self.click_on_signup_button()

    def get_error_message_email(self):
        return self.find_element(*self.locator.EMAIL_ERROR).text
