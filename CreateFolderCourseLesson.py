from BaseApp import BasePage
from selenium.webdriver.common.by import By
from BaseApp import BasePage
import time


# CreateFolderCourseLesson

class CreateCourseLokators:
    LOCATOR_CREATE_COURSE_IN_FOLDER_BUTTON = (By.LINK_TEXT, "Создать курс в папке")
    LOCATOR_NAME_OF_COURSE_FIELD = (By.XPATH, "//input[@id='title']")
    LOCATOR_DESCRIPTION_OF_COURSE_FIELD_IFRAME = (By.XPATH, "//iframe[@class='cke_wysiwyg_frame cke_reset']")
    LOCATOR_DESCRIPTION_OF_COURSE_FIELD_IFRAME_FIELD = (By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
    LOCATOR_CREATE_COURSE_BUTTON = (By.LINK_TEXT, "Создать курс")
    LOCATOR_CONTINUE_BUTTON = (By.LINK_TEXT, "Продолжить")
    LOCATOR_CHECK_CREATE_COURSE = (By.XPATH, "//div[@class='block__bigtitle js-bigtitle']")


class CreateLessonsLokators:
    LOCATOR_ADD_LESSON_BUTTON = (By.XPATH, "//button[contains(@class,'button js-popup-trigger')]")


class CreateCourseHelper(BasePage):

    def click_on_the_create_course_in_folder_button(self):
        self.find_element(CreateCourseLokators.LOCATOR_CREATE_COURSE_IN_FOLDER_BUTTON).click()
        time.sleep(3)

    def enter_name_of_course(self, name_course):
        search_field = self.find_element(CreateCourseLokators.LOCATOR_NAME_OF_COURSE_FIELD)
        search_field.send_keys(name_course)

    def enter_description_of_course(self, description_of_course):
        iframe_box = self.find_element(CreateCourseLokators.LOCATOR_DESCRIPTION_OF_COURSE_FIELD_IFRAME)
        self.switch_iframe(iframe_box)
        description_field = self.find_element(CreateCourseLokators.LOCATOR_DESCRIPTION_OF_COURSE_FIELD_IFRAME_FIELD)
        description_field.send_keys(description_of_course)
        self.switch_from_iframe()

    def click_on_the_create_course_button(self):
        self.find_element(CreateCourseLokators.LOCATOR_CREATE_COURSE_BUTTON).click()

    def click_on_the_continue_button(self):
        self.find_element(CreateCourseLokators.LOCATOR_CONTINUE_BUTTON).click()

    def login_check(self):
        check_create_course = self.find_element(CreateCourseLokators.LOCATOR_CHECK_CREATE_COURSE).text
        return check_create_course

    def full_create_course(self, name_course, description_of_course):
        self.find_element(CreateCourseLokators.LOCATOR_CREATE_COURSE_IN_FOLDER_BUTTON).click()
        search_field = self.find_element(CreateCourseLokators.LOCATOR_NAME_OF_COURSE_FIELD)
        search_field.send_keys(name_course)
        iframe_box = self.find_element(CreateCourseLokators.LOCATOR_DESCRIPTION_OF_COURSE_FIELD_IFRAME)
        self.switch_iframe(iframe_box)
        description_field = self.find_element(CreateCourseLokators.LOCATOR_DESCRIPTION_OF_COURSE_FIELD_IFRAME_FIELD)
        description_field.send_keys(description_of_course)
        self.switch_from_iframe()
        self.find_element(CreateCourseLokators.LOCATOR_CREATE_COURSE_BUTTON).click()
        self.find_element(CreateCourseLokators.LOCATOR_CONTINUE_BUTTON).click()


class CreateCourseAndCreateLessonTheoryHelper(BasePage):
    def click_on_the_add_lesson_button(self):
        self.find_element(CreateLessonsLokators.LOCATOR_ADD_LESSON_BUTTON).click()
