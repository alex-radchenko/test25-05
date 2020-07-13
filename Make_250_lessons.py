from selenium import webdriver
import time
import allure
import lorem

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
    driver.set_window_size(1024, 768)
#    "screenResolution": "1280x1024x24"
#    driver = webdriver.Chrome()

    driver.get('http://at.dev01.1iu.ru')
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//li[3]//a[1]").click()
    driver.find_element_by_name("email").send_keys(login_at)
    driver.find_element_by_name("password").send_keys(pass_at)
    driver.find_element_by_xpath("//button[@class='btn modal__btn']").click()

    driver.implicitly_wait(10)
    #driver.get('https://at.dev01.1iu.ru/account/profile')
    #driver.implicitly_wait(10)
    #assert driver.find_element_by_xpath("//input[@id='email']").get_attribute("value") == login_at
    driver.find_element_by_xpath("//*[contains(text(), 'Тестирование много уроков')]").click()
    cycle_count = 0
    while cycle_count < 1:
        driver.find_element_by_xpath("//href[contains(text(), 'Уроки')]").click()
        driver.find_element_by_xpath("//button[@class='button js-popup-trigger']").click()
        driver.find_element_by_xpath("//body/div/a[1]/span[2]").click()
        #driver.find_element_by_xpath("").click()
        driver.find_element_by_xpath("//input[@class='required']").send_keys(lorem.sentence())
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/div[3]/div[1]/div[3]/div[2]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/span[1]/span[1]/span[2]").click()
        driver.find_element_by_xpath("//html//body//div//div//div//div//div//div//div//form//div//div//div//div//textarea").send_keys(lorem.paragraph())
        driver.find_element_by_xpath("//span[@class='b-btn button fl-r js-submit']").click()
        driver.find_element_by_xpath("//a[@class='b-btn animate fl-l js-popup-close']").click()
        cycle_count += 1
        print(cycle_count)

    driver.quit()