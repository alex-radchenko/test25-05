import pytest
from selenium import webdriver
import remote_driver
import browsers
import allure
import time


def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store', default='mac',
                     help="Choose selenoid type: selenoidserv or selenoidmac")

@pytest.fixture(scope="function")
def browser(request):
    selenoid = request.config.getoption("selenoid")
    if selenoid == "serv":
        capabilities = remote_driver.browser
        browser = webdriver.Remote(
            command_executor=remote_driver.ip_selenoid_serv,
            desired_capabilities=capabilities)
        browser.maximize_window()
        browser.implicitly_wait(10)
    elif selenoid == "mac":
        capabilities = remote_driver.browser
        browser = webdriver.Remote(
            command_executor=remote_driver.ip_selenoid_mac,
            desired_capabilities=capabilities)
        browser.maximize_window()
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError("--selenoid should be mac or serv")
    yield browser
    browser.quit()