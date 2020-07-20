import time
import allure
import pytest
from selenium.webdriver.common.keys import Keys
from PIL import Image
import image_1

@allure.feature('TEST')
@allure.title("TEST")
@pytest.mark.order0
def test_site_test(browser):
    allure.step("Водим логин и пароль")
    login_at = "radwexe@mail.ru"
    pass_at = "111"
    browser.get('https://antitreningi.ru')

    browser.find_element_by_xpath("//li[3]//a[1]").click()
    browser.find_element_by_name("email").send_keys(login_at)
    browser.find_element_by_name("password").send_keys(pass_at)
    browser.find_element_by_xpath("//button[@class='btn modal__btn']").click()
    assert browser.find_element_by_link_text("Создать курс в папке").is_displayed() == True
    browser.save_screenshot('screenshot_1.png')
    file_1 = "screenshot_1.png"
    file_2 = "screenshot_2.png"

    if int(image_1.percentage_difference(file_1, file_2)) >= 1:
        a1 = Image.open(file_1)
        b1 = Image.open(file_2)
        c = image_1.graphic_difference(a1, b1)
        c.save('333.png')
        allure.attach.file("333.png", attachment_type=allure.attachment_type.PNG)
    # assert int(image_1.percentage_difference(file_1, file_2)) == 0
    # allure.attach.file('333.png', attachment_type=allure.attachment_type.PNG)

@allure.feature('Title')
@allure.title("Простой вход через форму login")
@pytest.mark.order1

def test_site_login_chrome(browser):
    login_at = "radwexe@mail.ru"
    pass_at = "111"

    browser.get('https://antitreningi.ru')

    browser.find_element_by_xpath("//li[3]//a[1]").click()
    browser.find_element_by_name("email").send_keys(login_at)
    browser.find_element_by_name("password").send_keys(pass_at)
    browser.find_element_by_xpath("//button[@class='btn modal__btn']").click()
    assert browser.find_element_by_link_text("Создать курс в папке").is_displayed() == True
    browser.save_screenshot('screenshot_1.png')
    file_1 = "screenshot_1.png"
    file_2 = "screenshot_2.png"

    if int(image_1.percentage_difference(file_1, file_2)) >= 1:
        print("Большая разница")
        a1 = Image.open(file_1)
        b1 = Image.open(file_2)
        c = image_1.graphic_difference(a1, b1)
        #c.save('333.png')

    #assert int(image_1.percentage_difference(file_1, file_2)) == 0
    #allure.attach.file('333.png', attachment_type=allure.attachment_type.PNG)



@allure.feature('Title')
@allure.title("Создание курса")
@pytest.mark.order2
def test_site_create_kurs(browser):

    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")
    browser.implicitly_wait(10)
    # Create_cours
    browser.find_element_by_link_text("Создать курс в папке").click()
    browser.find_element_by_xpath("//input[@id='title']").send_keys("Название курса")
    browser.find_element_by_xpath("//div[@class='diary-settings__descr__wrap']//span[2]").click()
    browser.find_element_by_xpath("//textarea[@class='js-editor js-description-field js-editor-newformats']").send_keys(
        "Описание курса")
    browser.find_element_by_link_text("Создать курс").click()
    time.sleep(1)
    browser.find_element_by_link_text("Продолжить").click()
    assert browser.find_element_by_xpath("//div[@class='block__bigtitle js-bigtitle']").text == "Название курса"
    browser.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()

@allure.feature('Title')
@allure.title("Создание урока - Теория")
@pytest.mark.order3
def test_site_create_lesson_theory(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")
    browser.implicitly_wait(10)
    # Create_lesson_theory

    browser.find_element_by_link_text("Название курса").click()
    browser.find_element_by_link_text("Уроки").click()
    browser.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()
    browser.find_element_by_xpath("//div[@id='pu_lestype']//a[1]").click()
    browser.find_element_by_xpath("//input[@id='title']").send_keys("Урок №1")
    browser.find_element_by_xpath("//div[@class='diary-settings__descr__wrap']//span[2]").click()
    browser.find_element_by_xpath("//textarea[contains(@class,'js-editor js-description-field')]").send_keys(
        "Описание урока")
    browser.find_element_by_tag_name('body').send_keys(Keys.END)
    browser.find_element_by_xpath("//span[@class='b-btn button fl-r js-submit']").click()
    browser.find_element_by_xpath("//a[@class='b-btn animate fl-l js-popup-close']").click()

@allure.feature('Title')
@allure.title("Создание урока - Задание - Тип - Текстовый отчет")
@pytest.mark.order4
def test_site_create_lesson_task_type_1_text_report(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")
    # Create_lesson_task
    browser.find_element_by_link_text("Название курса").click()
    browser.find_element_by_link_text("Уроки").click()
    browser.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()
    browser.find_element_by_xpath("//div[@id='pu_lestype']//a[2]").click()
    for x in browser.find_elements_by_xpath(
            "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
        x.click()

    browser.find_element_by_xpath("//textarea[@name='lesson[description]']").send_keys(
        "Добавить теоретический блок_text")
    browser.find_element_by_xpath("//textarea[@name='lesson[curator_comment]']").send_keys(
        "Добавить инструкцию для наставника_text")

    # Добавить задание
    browser.find_element_by_id("select2-chosen-4").click()
    browser.find_element_by_xpath("//li[1]//div[1]").click()
    browser.find_element_by_xpath("//span[@class='b-btn button js-task-actions-button']").click()
    browser.find_element_by_xpath("//a[@class='cke_button cke_button__source cke_button_off']").click()

    browser.find_element_by_xpath("//span[@class='js-toggleInput']").click()
    browser.find_element_by_name("lesson[questions][0][question]").send_keys("Текст вопроса - Текстовый отчет")

    browser.find_element_by_xpath("//input[@id='title']").send_keys(
        "Название урока - task_type_1_text_report" + Keys.TAB + Keys.TAB + Keys.TAB + "Пояснение для вопроса task_type_1_text_report")
    browser.find_element_by_xpath("//span[@class='b-btn button fl-r js-submit']").click()

@allure.feature('Title')
@allure.title("Создание урока - Задание - Тип - Заполнение пробелов")
@pytest.mark.order5
def test_site_create_lesson_task_type_2_filling_the_gaps(browser):
    browser.implicitly_wait(10)
    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")
    # Create_lesson_task
    browser.find_element_by_link_text("Название курса").click()
    browser.find_element_by_link_text("Уроки").click()
    browser.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()
    browser.find_element_by_xpath("//div[@id='pu_lestype']//a[2]").click()
    for x in browser.find_elements_by_xpath(
            "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
        x.click()

    browser.find_element_by_xpath("//textarea[@name='lesson[description]']").send_keys(
        "Добавить теоретический блок task_type_2_filling_the_gaps")
    browser.find_element_by_xpath("//textarea[@name='lesson[curator_comment]']").send_keys(
        "Добавить инструкцию для наставника task_type_2_filling_the_gaps")

    # Добавить задание
    browser.find_element_by_id("select2-chosen-4").click()
    browser.find_element_by_xpath("//li[2]//div[1]").click()
    browser.find_element_by_xpath("//span[@class='b-btn button js-task-actions-button']").click()
    browser.find_element_by_xpath("//a[@class='cke_button cke_button__source cke_button_off']").click()

    browser.find_element_by_xpath("//span[@class='js-toggleInput']").click()
    browser.find_element_by_name("lesson[questions][0][question]").send_keys(
        "Текст вопроса - task_type_2_filling_the_gaps")

    browser.find_element_by_xpath("//input[@id='title']").send_keys(
        "Название урока - task_type_2_filling_the_gaps" + Keys.TAB + Keys.TAB + Keys.TAB + "Пояснение для вопроса task_type_2_filling_the_gaps ###")

    browser.find_element_by_xpath("//span[@class='b-btn button fl-r js-submit']").click()

@allure.feature('Title')
@allure.title("Создание урока - Задание - Тип - Загрузка файлов")
@pytest.mark.order6
def test_site_create_lesson_task_type_3_upload_file(browser):

    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")
    # Create_lesson_task
    browser.find_element_by_link_text("Название курса").click()
    browser.find_element_by_link_text("Уроки").click()
    browser.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()
    browser.find_element_by_xpath("//div[@id='pu_lestype']//a[2]").click()
    for x in browser.find_elements_by_xpath(
            "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
        x.click()

    browser.find_element_by_xpath("//textarea[@name='lesson[description]']").send_keys(
        "Добавить теоретический блок task_type_3_upload_file")
    browser.find_element_by_xpath("//textarea[@name='lesson[curator_comment]']").send_keys(
        "Добавить инструкцию для наставника task_type_3_upload_file")

    # Добавить задание
    browser.find_element_by_id("select2-chosen-4").click()
    browser.find_element_by_xpath("//li[3]//div[1]").click()
    browser.find_element_by_xpath("//span[@class='b-btn button js-task-actions-button']").click()
    browser.find_element_by_xpath("//a[@class='cke_button cke_button__source cke_button_off']").click()

    browser.find_element_by_xpath("//span[@class='js-toggleInput']").click()
    browser.find_element_by_name("lesson[questions][0][question]").send_keys("Текст вопроса - task_type_3_upload_file")

    browser.find_element_by_xpath("//input[@id='title']").send_keys(
        "Название урока - task_type_3_upload_file" + Keys.TAB + Keys.TAB + Keys.TAB + "Пояснение для вопроса task_type_3_upload_file")

    browser.find_element_by_xpath("//span[@class='b-btn button fl-r js-submit']").click()

@allure.feature('Title')
@allure.title("Создание урока - Задание - Тип - Голосовое сообщение")
@pytest.mark.order7
def test_site_create_lesson_task_type_4_upload_voice_message(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")
    # Create_lesson_task
    browser.find_element_by_link_text("Название курса").click()
    browser.find_element_by_link_text("Уроки").click()
    browser.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()
    browser.find_element_by_xpath("//div[@id='pu_lestype']//a[2]").click()
    for x in browser.find_elements_by_xpath(
            "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
        x.click()

    browser.find_element_by_xpath("//textarea[@name='lesson[description]']").send_keys(
        "Добавить теоретический блок task_type_4_upload_voice_message")
    browser.find_element_by_xpath("//textarea[@name='lesson[curator_comment]']").send_keys(
        "Добавить инструкцию для наставника task_type_4_upload_voice_message")

    # Добавить задание
    browser.find_element_by_id("select2-chosen-4").click()
    browser.find_element_by_xpath("//li[4]//div[1]").click()
    browser.find_element_by_xpath("//span[@class='b-btn button js-task-actions-button']").click()
    browser.find_element_by_xpath("//a[@class='cke_button cke_button__source cke_button_off']").click()

    browser.find_element_by_xpath("//span[@class='js-toggleInput']").click()
    browser.find_element_by_name("lesson[questions][0][question]").send_keys("Текст вопроса - task_type_4_voice_message")

    browser.find_element_by_xpath("//input[@id='title']").send_keys(
        "Название урока - task_type_3_upload_voice_message" + Keys.TAB + Keys.TAB + Keys.TAB + "Пояснение для вопроса task_type_4_upload_voice_message")

    browser.find_element_by_xpath("//span[@class='b-btn button fl-r js-submit']").click()
    time.sleep(3)

#@pytest.mark.order8
#def test_site_create_lesson_task_type_5_statistics(browser):
#    assert 2 == 2

#    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")
#    # Create_lesson_task
#    browser.find_element_by_link_text("Название курса").click()
#    browser.find_element_by_link_text("Уроки").click()
#    browser.find_element_by_xpath("//button[contains(@class,'button js-popup-trigger')]").click()
#    browser.find_element_by_xpath("//div[@id='pu_lestype']//a[2]").click()
#    for x in browser.find_elements_by_xpath(
#            "//span[@class='b-btn button button_light button_blank js-description_toggler']"):
#        x.click()
#
#    browser.find_element_by_xpath("//textarea[@name='lesson[description]']").send_keys(
#        "Добавить теоретический блок task_type_5_statistics")
#    browser.find_element_by_xpath("//textarea[@name='lesson[curator_comment]']").send_keys(
#        "Добавить инструкцию для наставника task_type_5_statistics")
#
#    # Добавить задание
#    browser.find_element_by_id("select2-chosen-4").click()
#    browser.find_element_by_xpath("//li[4]//div[1]").click()
#    browser.find_element_by_xpath("//button[@class='button js-more']").click()
#    browser.find_element_by_xpath("//input[@class='js-task-stats-newname']").send_keys("Название показателя")



@allure.feature('Удаление')
@allure.title("Удаление всех курсов")
@pytest.mark.order9
def test_site_delete_cours(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")

    for sel_del in browser.find_elements_by_xpath(
            "//body//div[@id='courseslist']//div//div[3]//div[1]//div[3]//div[1]//div[2]//div[1]//div[1]//img[1]"):
        browser.implicitly_wait(10)
        sel_del.click()
        browser.find_element_by_xpath(
            "//div[contains(@class,'MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-xs-space-between')]//div[1]//div[1]//div[1]//button[1]//span[1]").click()
        time.sleep(3)

@allure.feature('Удаление')
@allure.title("Удаление курсов из корзины")
@pytest.mark.order10
def test_site_delete_cours_from_basket(browser):
    browser.get("https://antitreningi.ru/account/auth?&token=6auklaju4ccqs4vuj4a48vfvoe")

    for sel_del in browser.find_elements_by_xpath(
            "//body//div[@id='courseslist']//div//div[3]//div[1]//div[4]//div[1]//div[2]//div[1]//div[1]//img[1]"):
        browser.implicitly_wait(10)
        sel_del.click()
        browser.find_element_by_xpath(
            "//div[contains(@class,'MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-xs-space-between')]//div[1]//div[1]//div[1]//button[1]//span[1]").click()