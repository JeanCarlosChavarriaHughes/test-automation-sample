# Test Automation Sample

This repository contains the source code for testing basic functionalities of Practice Test Automation Web Page (SUT).
[Public web site under test](https://practicetestautomation.com/practice-test-login/)

The project is structured by following the Page Object Model design pattern, which represents each page in the SUT as a separate class, and separately the corresponding test cases.

## Structure

*Pages*
* [Base Page](../pages/base_page.py)
* [Login Page](../pages/login_page.py)

*Tests*
* [conftests.py](../tests/conftest.py): this file contains the pytest fixture common for all tests. In this case the driver initialization and finalization, developed with the yield approach.
* [test login page](../tests/test_login.py) These are the automated test cases designed for the basic login page.
  * test_login_success
  * test_login_invalid
  * test_expected_url