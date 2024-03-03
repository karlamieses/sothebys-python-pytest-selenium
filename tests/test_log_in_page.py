from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

from pages.landing_page import LandingPage
from pages.signup_page import SignupPage
from pages.base_page import BasePage
from utils.locators import LogOutLocator


def test_valid_user_can_login(driver):
    landing_page = LandingPage(driver)
    base_page = BasePage(driver)
    signup_page = SignupPage(driver)

    landing_page.click_login_button()
    signup_page.enter_email(email)
    signup_page.enter_password(password)
    signup_page.click_on_signup_button()
    base_page.wait_until_element_is_not_present(LogOutLocator.PREFERRED_ACCESS)

    base_page.wait_for_page_to_load('https://www.sothebys.com/en')