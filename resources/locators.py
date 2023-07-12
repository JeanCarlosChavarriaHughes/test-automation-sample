from selenium.webdriver.common.by import By

class LoginPageLocators():
    input_login_username = (By.ID, "username")
    input_login_password = (By.ID, "password")
    button_submit = (By.ID, "submit")
    login_hint = (By.CLASS_NAME, "show")