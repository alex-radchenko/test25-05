import allure
import pytest
from selenium import webdriver
import remote_driver

@pytest.fixture(scope="function")
def browser():
    capabilities = remote_driver.browser
    driver = webdriver.Remote(
        command_executor=remote_driver.ip_selenoid,
        desired_capabilities=capabilities)
    driver.maximize_window()
    allure.enviroment()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
