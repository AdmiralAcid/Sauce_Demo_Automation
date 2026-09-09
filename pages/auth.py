from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base

class Auth(Base):

    url = 'https://www.saucedemo.com'
    #driver = webdriver.Chrome()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print('Start auth')

    # locators
    username_loc = 'user-name'
    password_loc = 'password'
    login_loc = 'login-button'
    title_loc = '//span[@class="title"]'

    # getters
    def get_username(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.username_loc)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.password_loc)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.login_loc)))

    def get_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.title_loc)))

    # actions
    def input_username(self, payload):
        self.get_username().send_keys(payload)
        print('Login input')

    def input_password(self, payload):
        self.get_password().send_keys(payload)
        print('Password input')

    def auth_click(self):
        self.get_login_button().click()
        print('Login in')

    def authorization(self, username, passw):
        with allure.step("Authorization"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            print(f'current URL is {self.get_url()}')
            self.input_username(username)
            self.input_password(passw)
            self.auth_click()
            self.assert_word(self.get_title(), 'Products')
