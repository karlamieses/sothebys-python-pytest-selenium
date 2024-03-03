
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.locators import MainPageLocator
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://www.sothebys.com/en/')

cookies = [
    {
        'name': 'OptanonAlertBoxClosed',
        'value': '2024-03-03T18:41:39.793Z'
    }, {
        'name': 'ajs_anonymous_id',
        'value': '024198a2-b234-436f-9ee6-30988b3507a8'
    }]

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()


driver.implicitly_wait(30)

driver.find_element(*MainPageLocator.LOGO).click()

landing_page = LandingPage(driver)
signup_page = SignupPage(driver)

landing_page.click_login_button()

login_page =LoginPage(driver)
login_page.click_signup_button()
signup_page.sign_up_with_invalid_user()

# driver.find_element(*MainPageLocator.LOGIN_BUTTON).click()
