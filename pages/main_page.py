from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print('Opening main page')

    # locators
    backpack_button_loc = 'add-to-cart-sauce-labs-backpack'
    bike_light_loc = 'add-to-cart-sauce-labs-bike-light'
    jacket_loc = 'add-to-cart-sauce-labs-fleece-jacket'
    shopping_cart_loc = '//a[@data-test="shopping-cart-link"]'
    burger_loc = 'react-burger-menu-btn'
    burger_about_loc = 'about_sidebar_link'

    # getters
    def get_backpack_add(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.backpack_button_loc)))

    def get_bike_light_add(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.bike_light_loc)))

    def get_jacket_add(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.jacket_loc)))

    def get_shopping_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.shopping_cart_loc)))

    def get_burger(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.burger_loc)))

    def get_burger_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.burger_about_loc)))

    # actions
    def add_backpack(self):
        self.get_backpack_add().click()
        print('Backpack is added')

    def add_bike_light(self):
        self.get_bike_light_add().click()
        print('Bike light is added')

    def add_jacket(self):
        self.get_jacket_add().click()
        print('Fleece Jacket is added')

    def open_shopping_cart(self):
        self.get_shopping_cart().click()
        print('Going into shopping cart')

    def open_burger(self):
        self.get_burger().click()
        print('Going into menu')

    def open_burger_about(self):
        self.get_burger_about().click()
        print('Opening "About" link')

    def select_backpack(self):
        with allure.step("Select backpack"):
            print(f'current URL is {self.get_url()}')
            self.add_backpack()
            self.open_shopping_cart()

    def select_bike_light(self):
        with allure.step("Select bike light"):
            print(f'current URL is {self.get_url()}')
            self.add_bike_light()
            self.open_shopping_cart()

    def select_jacket(self):
        with allure.step("Select jacket"):
            print(f'current URL is {self.get_url()}')
            self.add_jacket()
            self.open_shopping_cart()

    def select_menu_about(self):
        print(f'current URL is {self.get_url()}')
        self.open_burger()
        self.open_burger_about()
