from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        """doc
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title) -> str:
        """doc
        """
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
    
    def get_text(self, by_locator) -> str:
        """doc
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        
