import pytest
from selenium import webdriver
import remote_driver
import browsers
import allure
import time

def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store', default=None,
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    selenoid = request.config.getoption("selenoid_type")
    capabilities = None
    browser = None
    if selenoid == "selenoidserv":
        capabilities = remote_driver.browser
        browser = webdriver.Remote(
            command_executor=remote_driver.ip_selenoid_serv,
            desired_capabilities=capabilities)
        browser.maximize_window()
        browser.implicitly_wait(10)
        yield browser
        browser.quit()
    elif selenoid == "selenoidmac":
        capabilities = remote_driver.browser
        browser = webdriver.Remote(
            command_executor=remote_driver.ip_selenoid_mac,
            desired_capabilities=capabilities)
        browser.maximize_window()
        browser.implicitly_wait(10)
        yield browser
        browser.quit()
    else:
        raise pytest.UsageError("--selenoid_type should be ip_selenoid_mac or ip_selenoid_serv")
    yield browser
    browser.quit()
