from utils.urls import URLs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, base_url=URLs.BASE_URL):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, *locator, index=None):
        if index is None:
            self.wait_element(*locator)
            return self.driver.find_element(*locator)
        else:
            elements = self.driver.find_elements(*locator)
            return elements[index] if 0 <= index < len(elements) else None

    def wait_element(self, *locator, index=None):
        if index is None:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        else:
            WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_elements(*locator)[index])

    def launch_url(self):
        self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def wait_until_element_is_not_present(self, *locator):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(*locator))

    def wait_for_page_to_load(self, expected_url):
        return WebDriverWait(self.driver, 15).until(EC.url_matches(expected_url))

    def retrieve_text(self, *locator):
        get_text = self.find_element(*locator)
        retrieved_text = get_text.text
        return retrieved_text


