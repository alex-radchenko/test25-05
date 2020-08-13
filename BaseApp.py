from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helper


class BasePage:
    def __init__(self, browser):
        self.driver = browser
        self.base_url = "https://antitreningi.ru"
        self.base_url_token = "https://antitreningi.ru/account/auth?&token=" + helper.token

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_site_through_token(self):
        return self.driver.get(self.base_url_token)
