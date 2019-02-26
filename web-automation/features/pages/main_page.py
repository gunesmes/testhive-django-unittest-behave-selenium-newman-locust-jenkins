from .base_page import BasePage
from selenium.webdriver.common.by import By
from support.users import get_user
import time


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes
class MainPage(BasePage):
    # Web elements on Main Page
    LOGO = (By.CSS_SELECTOR, '.topnav')
    USERS = (By.ID, 'users-nav')
    REGISTER = (By.ID, 'register-nav')
    USERS_TABLE = (By.ID, 'userListTable')
    USER_MODAL = (By.CSS_SELECTOR, '#myModal > .modal-content')

    def __init__(self, driver):
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.LOGO) else False

    def get_user_list(self):
        return self.find_element(*self.USERS_TABLE).text

    def click_register_button(self):
        self.find_element(*self.REGISTER).click()

    def click_users_button(self):
        self.find_element(*self.USERS).click()

    def check_users(self, usernames):
        for username in usernames:
            assert username in self.find_element(*self.USERS_TABLE).text

    def click_user(self, username):
        self.find_element(By.CSS_SELECTOR, '#%s > a' % username).click()

    def check_user_info(self, username):
        user_info = get_user(username)
        user_info_on_page = self.find_element(*self.USER_MODAL).text
        for key, value in user_info.items():
            assert value in user_info_on_page
