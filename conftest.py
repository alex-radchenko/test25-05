import pytest
from selenium import webdriver
import remote_driver
import browsers
import allure
import time


@pytest.fixture(scope="function")
def browser(request):
    selenoid_type = request.config.getoption("selenoid_type")
    capabilities = None
    driver = None
    if selenoid_type == "ip_selenoid_serv":
        capabilities = remote_driver.browser
        driver = webdriver.Remote(
            command_executor=remote_driver.ip_selenoid_serv,
            desired_capabilities=capabilities)
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    elif selenoid_type == "ip_selenoid_mac":
        capabilities = remote_driver.browser
        driver = webdriver.Remote(
            command_executor=remote_driver.ip_selenoid_mac,
            desired_capabilities=capabilities)
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    else:
        raise pytest.UsageError("--selenoid_type should be ip_selenoid_mac or ip_selenoid_serv")
    yield browser
    driver.quit()
