from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes


class MainPage(BasePage):
  # Web elements on Main Page
  LOGO          = (By.CSS_SELECTOR, '.topnav')
  USERS         = (By.ID, 'users-nav')
  REGISTER      = (By.ID, 'register-nav')
  USERS_TABLE   = (By.ID, 'userListTable')

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