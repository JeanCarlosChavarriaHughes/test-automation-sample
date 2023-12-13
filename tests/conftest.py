from sys import executable
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage

def page_object_init(request, driver):
    request.cls.login_page = LoginPage(driver)


@pytest.fixture()
def edge_driver_init(request):
    service = Service(executable_path="../drives/msedgedriver")
    driver = webdriver.Edge(service=service)
    request.cls.driver = driver
    page_object_init(request, driver)
    driver.get('https://practicetestautomation.com/practice-test-login/')
    driver.maximize_window()
    yield
    driver.quit()