from selenium.webdriver.common.by import By
from pages.main_page import MainPage


class RegisterPage(MainPage):
    # Web elements on Main Page
    LOGO          = (By.CSS_SELECTOR, '.topnav')
    USERNAME      = (By.ID, 'username')
    EMAIL         = (By.ID, 'email')
    BIRTHDAY      = (By.ID, 'birthday')
    ADDRESS       = (By.ID, 'address')
    REGISTER_BTN  = (By.ID, 'registerbtn')
    WARNING       = (By.ID, 'info')

    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver)  # Python2 version

    def check_page_loaded(self):
        return True if self.find_element(*self.LOGO) else False
 
    def enter_email(self, val):
        self.find_element(*self.EMAIL).clear()
        self.find_element(*self.EMAIL).send_keys(val)

    def enter_username(self, val):
        self.find_element(*self.USERNAME).clear()
        self.find_element(*self.USERNAME).send_keys(val)
    
    def enter_birthday(self, val):
        #self.find_element(*self.BIRTHDAY).clear()
        self.find_element(*self.BIRTHDAY).send_keys(val)

    def enter_address(self, val):
        self.find_element(*self.ADDRESS).clear()
        self.find_element(*self.ADDRESS).send_keys(val)

    def submit_register_form(self):
        self.find_element(*self.REGISTER_BTN).click()

    def get_message(self):
        return self.find_element(*self.WARNING).text

    def get_validation_message(self):
        elems = self.find_elements(By.CSS_SELECTOR, 'input')

        message = ''
        for elem in elems:
            print(elem.get_attribute("validationMessage"))
            message += str(elem.get_attribute("validationMessage"))
        return str(message)