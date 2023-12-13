import re
import pytest


class TestLogin():
    @pytest.mark.usefixtures('edge_driver_init')
    def test_login_success(self):
        usr = "student"
        pwd = "Password123"
        expected_title = r'Logged In Successfully | Practice Test Automation'

        self.login_page.submit_login(username=usr, password=pwd)

        actual_title = self.login_page.get_title(title=expected_title)
        assert re.match(expected_title, actual_title)
    
    @pytest.mark.usefixtures('edge_driver_init')
    def test_login_invalid(self):
        usr = "BadUser"
        pwd = "BadPass"
        expected_hint = r'Your username is invalid!'

        self.login_page.submit_login(username=usr, password=pwd)

        actual_hint = self.login_page.get_hint()
        assert re.match(expected_hint, actual_hint)

    @pytest.mark.usefixtures('edge_driver_init')
    def test_expected_url(self):
        expected_url = "https://practicetestautomation.com/practice-test-loginbadd"
        matching_url = self.login_page.check_url(expected_url)
        assert (matching_url)