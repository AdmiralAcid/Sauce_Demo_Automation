from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CheckoutInfo(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print('Start auth')

    # locators
    first_name_loc = 'first-name'
    last_name_loc = 'last-name'
    zip_code_loc = 'postal-code'
    continue_button_loc = 'continue'

    # getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.first_name_loc)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.last_name_loc)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.zip_code_loc)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.continue_button_loc)))

    # actions
    def input_first_name(self, payload):
        self.get_first_name().send_keys(payload)
        print('First name input')

    def input_last_name(self, payload):
        self.get_last_name().send_keys(payload)
        print('Last name input')

    def input_zip_code(self, payload):
        self.get_zip_code().send_keys(payload)
        print('Zip code input')

    def continue_click(self):
        self.get_continue_button().click()
        print('Continue button click')

    def info_filling_in(self, first_name, last_name, zip_code):
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_zip_code(zip_code)
        self.continue_click()
