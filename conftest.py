import pytest
from selenium import webdriver
import remote_driver
import allure

@pytest.fixture(scope="function")
def browser():
    capabilities = remote_driver.browser
    driver = webdriver.Remote(
        command_executor=remote_driver.ip_selenoid,
        desired_capabilities=capabilities)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    allure.environment(
        url='example.com',
        browser=u'Google Chrome',
        environment="production",
    )
