from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class BasePage():
    """documentation
    """

    def __init__(self, driver):
        """doc
        """
        self.driver = driver

    def click(self, by_locator):
        """doc
        """
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        """doc
        """
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title) -> str:
        """doc
        """
        WebDriverWait(self.driver, 15).until(EC.title_is(title))
        return self.driver.title
    
    def get_text(self, by_locator) -> str:
        """doc
        """
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).text

    def check_url(self, expected_url) -> str:
        """doc
        """
        try:
            return WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
        except TimeoutException as E:
            return False
        
