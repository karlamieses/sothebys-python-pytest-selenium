from selenium.webdriver.common.by import By


class MainPageLocator:
    LOGO = (By.CLASS_NAME, "PageLogo-image")
    LOGIN_BUTTON = (By.CLASS_NAME, 'SothebysHat-aemLogin')


class LoginPageLocator:
    SIGN_UP = (By.CSS_SELECTOR, '[id="footer"] a')


class SignUpPageLocator:
    EMAIL = (By.ID, 'email')
    EMAIL_ERROR = (By.ID, 'email-error')
    PASSWORD = (By.ID, 'password')
    PASSWORD_ERROR = (By.ID, 'password-error')
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    TITLE_LABEL = (By.ID, 'title-label')
    TITLE_LABEL_OPTION_MISS = (By.CSS_SELECTOR, '[data-value="Miss"]')
    TERMS_CHECK = (By.ID, 'termsCheck')
    SIGN_UP_BUTTON = (By.ID, 'login-button-id')


class LogOutLocator:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-text-content="Log Out"]')
    PREFERRED_ACCESS = (By.CSS_SELECTOR, '[data-text-content="Preferred Access"]')


class SearchLocator:
    SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, '[placeholder="Search Sotheby\'s"]')
    NUMBER_OF_RESULTS = (By.CLASS_NAME, 'searchStats')
