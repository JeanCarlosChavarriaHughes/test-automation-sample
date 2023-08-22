# test with pytest
# from tests.base_test import BaseTest
import re
# import pytest
from pages.login_page import LoginPage

#@pytest.mark.usefixtures('set_up')
#class TestLogin(BaseTest):

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service(executable_path="../drives/msedgedriver")
driver = webdriver.Edge(service=service)


def test_login_success():
    usr = "student"
    pwd = "Password123"
    expected_title = r'Logged In Successfully | Practice Test Automation'

    loginPage = LoginPage(driver=driver)

    loginPage.submit_login(username=usr, password=pwd)

    actual_title = loginPage.get_title(title=expected_title)
    assert re.match(expected_title, actual_title)