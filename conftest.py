import remote_driver
import browsers
from selenium import webdriver
import time
import pytest
import json
import re
# import lorem
from selenium.webdriver.common.keys import Keys


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