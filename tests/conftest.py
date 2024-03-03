import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.base_page import BasePage

cookies = [
    {
        'name': 'OptanonAlertBoxClosed',
        'value': '2024-03-03T18:41:39.793Z'
    }, {
        'name': 'ajs_anonymous_id',
        'value': '024198a2-b234-436f-9ee6-30988b3507a8'
    }]


@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    # driver.quit()


@pytest.fixture(autouse=True)
def setup_before_tests(driver):
    base_page = BasePage(driver)
    base_page.launch_url()

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()