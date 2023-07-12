# test with pytest
# from tests.base_test import BaseTest
import re

from pages.login_page import LoginPage

#@pytest.mark.usefixtures('set_up')
#class TestLogin(BaseTest):

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service(executable_path="../drives/msedgedriver")
driver = webdriver.Edge(service=service)

def test_login_success():
    usr = "BadUser"
    pwd = "BadPass"
    expected_hint = r'Your username is invalid!'

    loginPage = LoginPage(driver=driver)

    loginPage.submit_login(username=usr, password=pwd)

    actual_hint = loginPage.get_hint()
    assert re.match(expected_hint, actual_hint)