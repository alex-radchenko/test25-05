from selenium import webdriver
import time
import pytest
import json
import re

#import lorem
from selenium.webdriver.common.keys import Keys

@pytest.mark.order1
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
    time.sleep(15)

@pytest.mark.order2
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

    driver.implicitly_wait(10)
    driver.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")

    #Create_cours

    driver.find_element_by_link_text("Создать курс в папке").click()
    driver.find_element_by_xpath("//input[@id='title']").send_keys("Название курса")
    driver.find_element_by_xpath("//div[@class='diary-settings__descr__wrap']//span[2]").click()
    driver.find_element_by_xpath("//textarea[@class='js-editor js-description-field js-editor-newformats']").send_keys("Описание курса")
    driver.find_element_by_link_text("Создать курс").click()
    time.sleep(1)
    driver.find_element_by_link_text("Продолжить").click()
    assert driver.find_element_by_xpath("//div[@class='block__bigtitle js-bigtitle']").text == "Название курса"
    driver.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()

    driver.quit()
    time.sleep(15)

@pytest.mark.order3
def test_site_create_lesson_theory():
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

    driver.implicitly_wait(10)
    driver.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")

    #Create_lesson_theory

    driver.find_element_by_link_text("Название курса").click()
    driver.find_element_by_link_text("Уроки").click()
    driver.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()
    driver.find_element_by_xpath("//div[@id='pu_lestype']//a[1]").click()
    driver.find_element_by_xpath("//input[@id='title']").send_keys("Урок №1")
    driver.find_element_by_xpath("//div[@class='diary-settings__descr__wrap']//span[2]").click()
    driver.find_element_by_xpath("//textarea[contains(@class,'js-editor js-description-field')]").send_keys("Описание урока")
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.find_element_by_xpath("//span[@class='b-btn button fl-r js-submit']").click()
    driver.find_element_by_xpath("//a[@class='b-btn animate fl-l js-popup-close']").click()
    driver.quit()
    time.sleep(15)

@pytest.mark.order4
def test_site_create_lesson_task():
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

    driver.implicitly_wait(10)
    driver.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")
    #Create_lesson_task
    driver.find_element_by_link_text("Название курса").click()
    driver.find_element_by_link_text("Уроки").click()
    driver.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()
    driver.find_element_by_xpath("//div[@id='pu_lestype']//a[2]").click()
    #driver.find_element_by_xpath("//input[@id='title']").send_keys("Название урока - tasks")
    for x in driver.find_elements_by_xpath("//span[@class='b-btn button button_light button_blank js-description_toggler']"):
        x.click()

    driver.find_element_by_xpath("//textarea[@name='lesson[description]']").send_keys("Добавить теоретический блок_text")
    driver.find_element_by_xpath("//textarea[@name='lesson[curator_comment]']").send_keys("Добавить инструкцию для наставника_text")

    #Добавить задание
    driver.find_element_by_id("select2-chosen-4").click()
    driver.find_element_by_xpath("//li[1]//div[1]").click()
    driver.find_element_by_xpath("//span[@class='b-btn button js-task-actions-button']").click()
    driver.find_element_by_xpath("//a[@class='cke_button cke_button__source cke_button_off']").click()

    driver.find_element_by_xpath("//span[@class='js-toggleInput']").click()
    driver.find_element_by_name("lesson[questions][0][question]").send_keys("Текст вопроса - Текстовый отчет")


    driver.find_element_by_xpath("//input[@id='title']").send_keys("Название урока - tasks" + Keys.TAB + Keys.TAB + Keys.TAB + "Пояснение для вопроса")

    driver.find_element_by_xpath("//span[@class='b-btn button fl-r js-submit']").click()
    time.sleep(15)
    driver.quit()

@pytest.mark.order5
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

    driver.implicitly_wait(10)
    driver.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")

    for sel_del in driver.find_elements_by_xpath("//body//div[@id='courseslist']//div//div[3]//div[1]//div[3]//div[1]//div[2]//div[1]//div[1]//img[1]"):
        driver.implicitly_wait(10)
        sel_del.click()
        driver.find_element_by_xpath("//div[contains(@class,'MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-xs-space-between')]//div[1]//div[1]//div[1]//button[1]//span[1]").click()
        time.sleep(3)
    driver.quit()
    time.sleep(15)

@pytest.mark.order6
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

    driver.implicitly_wait(10)
    driver.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")

    for sel_del in driver.find_elements_by_xpath("//body//div[@id='courseslist']//div//div[3]//div[1]//div[4]//div[1]//div[2]//div[1]//div[1]//img[1]"):
        driver.implicitly_wait(10)
        sel_del.click()
        driver.find_element_by_xpath("//div[contains(@class,'MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-xs-space-between')]//div[1]//div[1]//div[1]//button[1]//span[1]").click()

    driver.quit()
    time.sleep(15)