from sys import executable
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BaseTest:
    @pytest.fixture(autouse=True)
    def set_up(self):
        print("initiating driver")
        service = Service(executable_path="../drives/msedgedriver")
        self.driver = webdriver.Edge(service=service)
        self.driver.implicitly_wait(10)
        print("---------------------")
        yield self.driver

        if self.driver is not None:
            print("---------------------")
            self.driver.close()
            self.driver.quit