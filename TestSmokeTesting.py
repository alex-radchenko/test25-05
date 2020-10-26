from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import requests
import bd_work
import time
import allure
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import selenium
from PIL import Image
import image_1
import helper
import os
import accounts
import locators
from MainPageLogin import MainPageHelper
from CreateFolderCourseLesson import CreateCourseHelper, CreateCourseAndCreateLessonTheoryHelper
import save_token

@allure.feature("TEST")
@allure.title("TEST")
@pytest.mark.order1
def test_site_test(browser):
    assert True

@allure.feature("Title")
@allure.title("Простой вход через форму login")
@pytest.mark.order2

def test_site_login_chrome(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.full_login(accounts.acc["radwexe"])
    main_page.login_check()

@allure.feature('Title')
@allure.title("Создание курса")
@pytest.mark.order3
def test_site_create_course(browser):
    create_course_page = CreateCourseHelper(browser)
    create_course_page.go_to_site_through_token()
    create_course_page.click_on_the_create_course_in_folder_button()
    create_course_page.enter_name_of_course("test_site_create_course")
    create_course_page.enter_description_of_course(create_course_page.enter_description_of_course.__name__)
    create_course_page.click_on_the_create_course_button()
    create_course_page.click_on_the_continue_button()
    assert create_course_page.login_check() == test_site_create_course.__name__

@allure.feature('Title')
@allure.title("Создание урока - Теория")
@pytest.mark.order4
def test_site_create_lesson_theory(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=" + save_token.token())
    # Create_lesson_theory

    browser.find_element(By.LINK_TEXT, test_site_create_course.__name__).click()

    browser.find_element(By.LINK_TEXT, "Уроки").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[contains(@class,'button js-popup-trigger')]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//div[@id='pu_lestype']//a[1]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@id='title']").send_keys("Урок №1")
    time.sleep(2)
    browser.find_element(By.XPATH, "//div[@class='diary-settings__descr__wrap']//span[2]").click()
    browser.find_element(By.XPATH, "//textarea[contains(@class,'js-editor js-description-field')]").send_keys(
        "Описание урока")
    browser.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)
    browser.find_element(By.XPATH, "//span[@class='b-btn button fl-r js-submit']").click()

@allure.feature('Title')
@allure.title("Создание урока - Задание - Тип - Текстовый отчет")
@pytest.mark.order5
def test_site_create_lesson_task_type_1_text_report(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=" + save_token.token())
    # Create_lesson_task
    browser.find_element(By.LINK_TEXT, test_site_create_course.__name__).click()
    browser.find_element(By.LINK_TEXT, "Уроки").click()
    browser.find_element(By.XPATH, "//button[contains(@class,'button js-popup-trigger')]").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[@id='pu_lestype']//a[2]").click()

    #вставка в iframe окно
    #browser.switch_to_frame(browser.find_element(By.XPATH, "(//iframe[@class='cke_wysiwyg_frame cke_reset'])[1]"))
    #browser.find_element(By.XPATH, "/html[1]/body[1]/p[1]").send_keys("Вставка")
    #browser.switch_to_default_content()
    # вставка в iframe окно
    browser.find_element(By.TAG_NAME, "iframe")
    for x in browser.find_elements(By.XPATH, "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
        x.click()

    browser.find_element(By.XPATH, "//textarea[@name='lesson[description]']").send_keys(
        "Добавить теоретический блок_text")
    browser.find_element(By.XPATH, "//textarea[@name='lesson[curator_comment]']").send_keys(
        "Добавить инструкцию для наставника_text")

    # Добавить задание
    # Old variant
    #browser.find_element(By.ID, "select2-chosen-4").click()
    # browser.find_element(By.XPATH, "//li[1]//div[1]").click()
    # Old variant
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_index("1")

    # _________

    browser.find_element(By.XPATH, "//span[@class='b-btn button js-task-actions-button']").click()
    browser.find_element(By.XPATH, "//a[@class='cke_button cke_button__source cke_button_off']").click()

    browser.find_element(By.XPATH, "//span[@class='js-toggleInput']").click()
    browser.find_element(By.NAME, "lesson[questions][0][question]").send_keys("Текст вопроса - Текстовый отчет")

    browser.find_element(By.XPATH, "//input[@id='title']").send_keys(
        "Название урока - task_type_1_text_report" + Keys.TAB + Keys.TAB + Keys.TAB + "Пояснение для вопроса task_type_1_text_report")
    browser.find_element(By.XPATH, "//span[@class='b-btn button fl-r js-submit']").click()


@allure.feature('Title')
@allure.title("Создание урока - Задание - Тип - Заполнение пробелов")
@pytest.mark.order6
def test_site_create_lesson_task_type_2_filling_the_gaps(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=" + save_token.token())
    # Create_lesson_task
    browser.find_element(By.LINK_TEXT, test_site_create_course.__name__).click()
    browser.find_element(By.LINK_TEXT, "Уроки").click()
    browser.find_element(By.XPATH, "//button[@class='button js-popup-trigger']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "(//a[@class='b-popup_lestype__link'])[2]").click()
    for x in browser.find_elements(By.XPATH, "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
        x.click()

    browser.find_element(By.XPATH, "//textarea[@name='lesson[description]']").send_keys(
        "Добавить теоретический блок task_type_2_filling_the_gaps")
    browser.find_element(By.XPATH, "//textarea[@name='lesson[curator_comment]']").send_keys(
        "Добавить инструкцию для наставника task_type_2_filling_the_gaps")

    # Добавить задание
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_index("2")
    browser.find_element(By.XPATH, "//span[@class='b-btn button js-task-actions-button']").click()
    browser.find_element(By.XPATH, "//a[@class='cke_button cke_button__source cke_button_off']").click()

    browser.find_element(By.XPATH, "//span[@class='js-toggleInput']").click()
    browser.find_element(By.NAME, "lesson[questions][0][question]").send_keys(
        "Текст вопроса - task_type_2_filling_the_gaps")

    browser.find_element(By.XPATH, "//input[@id='title']").send_keys(
        "Название урока - task_type_2_filling_the_gaps" + Keys.TAB + Keys.TAB + Keys.TAB + "Пояснение для вопроса task_type_2_filling_the_gaps ###")

    browser.find_element(By.XPATH, "//span[@class='b-btn button fl-r js-submit']").click()


@allure.feature('Title')
@allure.title("Создание урока - Задание - Тип - Загрузка файлов")
@pytest.mark.order7
def test_site_create_lesson_task_type_3_upload_file(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=" + save_token.token())
    # Create_lesson_task
    browser.find_element(By.LINK_TEXT, test_site_create_course.__name__).click()
    browser.find_element(By.LINK_TEXT, "Уроки").click()
    browser.find_element(By.XPATH, "//button[contains(@class,'button js-popup-trigger')]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//*[@data-type='task']").click()
    for x in browser.find_elements(By.XPATH, "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
        x.click()

    browser.find_element(By.XPATH, "//textarea[@name='lesson[description]']").send_keys(
        "Добавить теоретический блок task_type_3_upload_file")
    browser.find_element(By.XPATH, "//textarea[@name='lesson[curator_comment]']").send_keys(
        "Добавить инструкцию для наставника task_type_3_upload_file")

    # Добавить задание
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_index("3")
    browser.find_element(By.XPATH, "//span[@class='b-btn button js-task-actions-button']").click()
    browser.find_element(By.XPATH, "//a[@class='cke_button cke_button__source cke_button_off']").click()

    browser.find_element(By.XPATH, "//span[@class='js-toggleInput']").click()
    browser.find_element(By.NAME, "lesson[questions][0][question]").send_keys("Текст вопроса - task_type_3_upload_file")

    browser.find_element(By.XPATH, "//input[@id='title']").send_keys(
        "Название урока - task_type_3_upload_file" + Keys.TAB + Keys.TAB + Keys.TAB + "Пояснение для вопроса task_type_3_upload_file")

    browser.find_element(By.XPATH, "//span[@class='b-btn button fl-r js-submit']").click()


@allure.feature('Title')
@allure.title("Создание урока - Задание - Тип - Голосовое сообщение")
@pytest.mark.order8
def test_site_create_lesson_task_type_4_upload_voice_message(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=" + save_token.token())
    # Create_lesson_task
    browser.find_element(By.LINK_TEXT, test_site_create_course.__name__).click()
    browser.find_element(By.LINK_TEXT, "Уроки").click()
    browser.find_element(By.XPATH, "//button[contains(@class,'button js-popup-trigger')]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//div[@id='pu_lestype']//a[2]").click()
    for x in browser.find_elements(By.XPATH, "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
        x.click()

    browser.find_element(By.XPATH, "//textarea[@name='lesson[description]']").send_keys(
        "Добавить теоретический блок task_type_4_upload_voice_message")
    browser.find_element(By.XPATH, "//textarea[@name='lesson[curator_comment]']").send_keys(
        "Добавить инструкцию для наставника task_type_4_upload_voice_message")

    # Добавить задание
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_index("4")
    browser.find_element(By.XPATH, "//span[@class='b-btn button js-task-actions-button']").click()
    browser.find_element(By.XPATH, "//a[@class='cke_button cke_button__source cke_button_off']").click()

    browser.find_element(By.XPATH, "//span[@class='js-toggleInput']").click()
    browser.find_element(By.NAME, "lesson[questions][0][question]").send_keys(
        "Текст вопроса - task_type_4_voice_message")

    browser.find_element(By.XPATH, "//input[@id='title']").send_keys(
        "Название урока - task_type_3_upload_voice_message" + Keys.TAB + Keys.TAB + Keys.TAB + "Пояснение для вопроса task_type_4_upload_voice_message")

    browser.find_element(By.XPATH, "//span[@class='b-btn button fl-r js-submit']").click()
    time.sleep(3)


# @pytest.mark.order9
# def test_site_create_lesson_task_type_5_statistics(browser):
#    assert 2 == 2

#    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")
#    # Create_lesson_task
#    browser.find_element(By.LINK_TEXT, "Название курса").click()
#    browser.find_element(By.LINK_TEXT, "Уроки").click()
#    browser.find_element(By.XPATH, "//button[contains(@class,'button js-popup-trigger')]").click()
#    browser.find_element(By.XPATH, "//div[@id='pu_lestype']//a[2]").click()
#    for x in browser.find_elements_by_xpath(
#            "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
#        x.click()
#
#    browser.find_element(By.XPATH, "//textarea[@name='lesson[description]']").send_keys(
#        "Добавить теоретический блок task_type_5_statistics")
#    browser.find_element(By.XPATH, "//textarea[@name='lesson[curator_comment]']").send_keys(
#        "Добавить инструкцию для наставника task_type_5_statistics")
#
#    # Добавить задание
#    browser.find_element(By.ID, "select2-chosen-4").click()
#    browser.find_element(By.XPATH, "//li[4]//div[1]").click()
#    browser.find_element(By.XPATH, "//button[@class='button js-more']").click()
#    browser.find_element(By.XPATH, "//input[@class='js-task-stats-newname']").send_keys("Название показателя")

@allure.feature('Удаление')
@allure.title("Удаление всех курсов")
@pytest.mark.order10
def test_site_delete_cours(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=" + save_token.token())
    browser.find_element(By.XPATH,"(//*[contains(@title, 'Удалить курс')])[1]").click()
    browser.find_element(By.XPATH,
                "//div[contains(@class,'MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-xs-space-between')]//div[1]//div[1]//div[1]//button[1]").click()
    time.sleep(1)

#
#    for sel_del in browser.find_elements(By.XPATH, "//div[contains(@class,'MuiBox-root jss133 styles--courseParamsLinkWrap__2eR7X jss118')]//img[contains(@class,'')]"):
#        sel_del.click()
#        time.sleep(3)
#        browser.find_element(By.XPATH,
#            "//div[contains(@class,'MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-xs-space-between')]//div[1]//div[1]//div[1]//button[1]").click()
#        time.sleep(1)


#@allure.feature('Удаление')
#@allure.title("Удаление курсов из корзины")
#@pytest.mark.order11
#def test_site_delete_cours_from_basket(browser):
#    browser.get("https://antitreningi.ru/account/auth?&token=" + save_token.token())
#    browser.find_element(By.XPATH, "//div[@title='Корзина']").click() if browser.find_element(By.XPATH, "//img[contains(@class, 'svgicon svgicon-courses-expand   ')]").get_attribute("class") == "svgicon svgicon-courses-expand   " else None
#    for sel_del in browser.find_elements(By.XPATH, "//div[@title='Удалить курс']"):
#        sel_del.click()
#        time.sleep(3)
#        browser.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
#        time.sleep(2)