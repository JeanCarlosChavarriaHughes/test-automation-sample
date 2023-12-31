from pages.base_page import BasePage
from resources.locators import LoginPageLocators as lpc

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # driver.get was moved to conftest
        # self.driver.get('https://practicetestautomation.com/practice-test-login/')

    def submit_login(self, username, password):
        self.enter_text(lpc.input_login_username, username)
        self.enter_text(lpc.input_login_password, password)
        self.click(lpc.button_submit)
    
    def get_hint(self):
        return self.get_text(lpc.login_hint)