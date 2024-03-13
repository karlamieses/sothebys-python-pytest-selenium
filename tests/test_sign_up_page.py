from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def test_error_message_when_email_address_is_incorrect(driver):
    landing_page = LandingPage(driver)
    login_page = LoginPage(driver)
    signup_page = SignupPage(driver)

    landing_page.click_login_button()
    login_page.click_signup_button()
    signup_page.enter_email("invalid_user")
    signup_page.click_on_signup_button()

    assert signup_page.get_error_message_email() == "Invalid email address"





