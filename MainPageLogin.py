from BaseApp import BasePage
from selenium.webdriver.common.by import By
import accounts
from BaseApp import BasePage
import time


class MainPageLoginLokators:
    LOCATOR_YELLOW_BUTTON_LOGIN = (By.XPATH, "//li[3]//a[1]")
    LOCATOR_EMAIL_FIELD = (By.NAME, "email")
    LOCATOR_PASSWORD_FIELD = (By.NAME, "password")
    LOCATOR_ENTER_BUTTON = (By.XPATH, "//button[@class='btn modal__btn']")
    LOCATOR_CHECK_CREATE_COURS = (By.LINK_TEXT, "Создать курс в папке")



class MainPageHelper(BasePage):

    def click_on_the_yellow_button(self):
        return self.find_element(MainPageLoginLokators.LOCATOR_YELLOW_BUTTON_LOGIN).click()

    def enter_email(self, email):
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_EMAIL_FIELD)
        search_field.send_keys(email)
        return search_field
    def enter_password(self, pas):
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_PASSWORD_FIELD)
        search_field.send_keys(pas)
        return search_field

    def click_on_the_enter_button(self):
        return self.find_element(MainPageLoginLokators.LOCATOR_ENTER_BUTTON).click()

    def full_login(self, acc):
        login = acc["login"]
        pas = acc["pass"]
        self.find_element(MainPageLoginLokators.LOCATOR_YELLOW_BUTTON_LOGIN).click()
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_EMAIL_FIELD)
        search_field.send_keys(login)
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_PASSWORD_FIELD)
        search_field.send_keys(pas)
        self.find_element(MainPageLoginLokators.LOCATOR_ENTER_BUTTON).click()
        return self

    def login_check(self):
        check_el = self.find_element(MainPageLoginLokators.LOCATOR_CHECK_CREATE_COURS)
        assert check_el.is_displayed() == True