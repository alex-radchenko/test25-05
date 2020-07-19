import remote_driver
from selenium import webdriver
import pytest
import allure
from allure_commons.types import AttachmentType



@pytest.fixture(scope="function")
def browser():
    capabilities = remote_driver.browser
    driver = webdriver.Remote(
        command_executor=remote_driver.ip_selenoid,
        desired_capabilities=capabilities)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    allure.attach("engine.title", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    driver.quit()
