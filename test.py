from selenium import webdriver
import time
import allure

def test_site_work():
    assert True

def test_site_work2():
    assert True

def test_site_login_chrome():
    login_at = "author@1iu.ru"
    pass_at = "dev"

    capabilities = {
        "browserName": "chrome",
        "version": "83.0",
        "enableVNC": True,
        "enableVideo": False
    }
    driver = webdriver.Remote(
        command_executor="http://128.199.103.130:4444/wd/hub",
        desired_capabilities=capabilities)
    driver.implicitly_wait(10)

    driver.get('http://at.dev01.1iu.ru')

    driver.find_element_by_xpath("//li[3]//a[1]").click()
    print("Кликнули")
    driver.find_element_by_name("email").send_keys(login_at)
    driver.find_element_by_name("password").send_keys(pass_at)
    driver.find_element_by_xpath("//button[@class='btn modal__btn']").click()
    driver.implicitly_wait(10)
    driver.get('https://at.dev01.1iu.ru/account/profile')
    driver.implicitly_wait(10)
    assert driver.find_element_by_xpath("//input[@id='email']").get_attribute("value") == login_at
    driver.quit()