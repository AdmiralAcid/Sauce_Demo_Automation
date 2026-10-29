from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base

class Auth(Base):

    url = 'https://www.saucedemo.com'

    def __init__(self, driver):
        super().__init__(driver)
        print('\nStart auth:')

    # locators
    username_loc = 'user-name'
    password_loc = 'password'
    login_loc = 'login-button'
    title_loc = '//span[@class="title"]'
    error_loc = '//h3[@data-test="error"]'
    close_msg_loc = 'error-button'

    # getters
    def get_username(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.username_loc)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.password_loc)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.login_loc)))

    def get_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.title_loc)))

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.error_loc)))

    def get_err_msg_close_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.close_msg_loc)))

    # actions
    def input_username(self, payload):
        self.get_username().send_keys(payload)
        print(f'Login {payload} input')

    def input_password(self, payload):
        self.get_password().send_keys(payload)
        print(f'Password {payload} input')

    def auth_click(self):
        self.get_login_button().click()
        print('Logging in')

    def check_error_text(self, error_text):
        err_txt = self.get_error_message().text
        assert error_text == err_txt

    def close_err_msg(self):
        self.get_err_msg_close_button().click()
        print('Closing error message')

    def authorization(self, username, passw):
        with allure.step("Authorization"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            print(f'current URL is {self.get_url()}')
            self.input_username(username)
            self.input_password(passw)
            self.auth_click()
            # self.assert_word(self.get_title(), 'Products')

    def try_to_skip_authorization(self, other_url):
        self.driver.get(other_url)
        self.driver.maximize_window()
        print(f'current URL is {self.get_url()}')