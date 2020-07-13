from selenium import webdriver
import time

#import lorem
from selenium.webdriver.common.keys import Keys

def test_site_login_chrome():
    capabilities = {
        "browserName": "chrome",
        "version": "83.0",
        "enableVNC": True,
        "enableVideo": False
    }
    driver = webdriver.Remote(
        command_executor="http://128.199.103.130:4444/wd/hub",
        desired_capabilities=capabilities)
    driver.maximize_window()

    login_at = "radwexe@mail.ru"
    pass_at = "111"

    driver.get('http://at.dev01.1iu.ru')
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//li[3]//a[1]").click()
    driver.find_element_by_name("email").send_keys(login_at)
    driver.find_element_by_name("password").send_keys(pass_at)
    driver.find_element_by_xpath("//button[@class='btn modal__btn']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_link_text("Создать курс в папке").click()
    driver.quit()

def test_site_create_cours():
    capabilities = {
        "browserName": "chrome",
        "version": "83.0",
        "enableVNC": True,
        "enableVideo": False
    }
    driver = webdriver.Remote(
        command_executor="http://128.199.103.130:4444/wd/hub",
        desired_capabilities=capabilities)
    driver.maximize_window()

    login_at = "radwexe@mail.ru"
    pass_at = "111"

    driver.get('http://at.dev01.1iu.ru')
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//li[3]//a[1]").click()
    driver.find_element_by_name("email").send_keys(login_at)
    driver.find_element_by_name("password").send_keys(pass_at)
    driver.find_element_by_xpath("//button[@class='btn modal__btn']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_link_text("Создать курс в папке").click()
    driver.find_element_by_xpath("//input[@id='title']").send_keys("Название курса")
    driver.find_element_by_xpath("//div[@class='diary-settings__descr__wrap']//span[2]").click()
    driver.find_element_by_xpath("//textarea[@class='js-editor js-description-field js-editor-newformats']").send_keys("Описание курса")
    driver.find_element_by_link_text("Создать курс").click()
    time.sleep(1)
    driver.find_element_by_link_text("Продолжить").click()
    assert driver.find_element_by_xpath("//div[@class='block__bigtitle js-bigtitle']").text == "Название курса"
    driver.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='pu_lestype']//a[1]").click()

    driver.find_element_by_xpath("//input[@id='title']").send_keys("Урок №1")
    driver.find_element_by_xpath("//div[@class='diary-settings__descr__wrap']//span[2]").click()

    driver.find_element_by_xpath("//textarea[contains(@class,'js-editor js-description-field')]").send_keys("Описание урока")

    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.find_element_by_xpath("//span[@class='b-btn button fl-r js-submit']").click()
    driver.find_element_by_xpath("//a[@class='b-btn animate fl-l js-popup-close']").click()
    time.sleep(3)

    driver.quit()

def test_site_delete_cours():
    capabilities = {
        "browserName": "chrome",
        "version": "83.0",
        "enableVNC": True,
        "enableVideo": False
    }
    driver = webdriver.Remote(
        command_executor="http://128.199.103.130:4444/wd/hub",
        desired_capabilities=capabilities)
    driver.maximize_window()

    login_at = "radwexe@mail.ru"
    pass_at = "111"

    driver.get('http://at.dev01.1iu.ru')
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//li[3]//a[1]").click()
    driver.find_element_by_name("email").send_keys(login_at)
    driver.find_element_by_name("password").send_keys(pass_at)
    driver.find_element_by_xpath("//button[@class='btn modal__btn']").click()
    driver.implicitly_wait(10)

    for sel_del in driver.find_elements_by_xpath("//body//div[@id='courseslist']//div//div[3]//div[1]//div[3]//div[1]//div[2]//div[1]//div[1]//img[1]"):
        driver.implicitly_wait(10)
        sel_del.click()
        driver.find_element_by_xpath("//div[contains(@class,'MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-xs-space-between')]//div[1]//div[1]//div[1]//button[1]//span[1]").click()
        time.sleep(3)
    time.sleep(3)
    driver.quit()

def test_site_delete_cours_from_basket():
    capabilities = {
        "browserName": "chrome",
        "version": "83.0",
        "enableVNC": True,
        "enableVideo": False
    }
    driver = webdriver.Remote(
        command_executor="http://128.199.103.130:4444/wd/hub",
        desired_capabilities=capabilities)
    driver.maximize_window()

    login_at = "radwexe@mail.ru"
    pass_at = "111"

    driver.get('http://at.dev01.1iu.ru')
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//li[3]//a[1]").click()
    driver.find_element_by_name("email").send_keys(login_at)
    driver.find_element_by_name("password").send_keys(pass_at)
    driver.find_element_by_xpath("//button[@class='btn modal__btn']").click()
    driver.implicitly_wait(10)

    for sel_del in driver.find_elements_by_xpath("//body//div[@id='courseslist']//div//div[3]//div[1]//div[4]//div[1]//div[2]//div[1]//div[1]//img[1]"):
        driver.implicitly_wait(10)
        sel_del.click()
        driver.find_element_by_xpath("//div[contains(@class,'MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-xs-space-between')]//div[1]//div[1]//div[1]//button[1]//span[1]").click()
        time.sleep(3)
    time.sleep(3)
    driver.quit()