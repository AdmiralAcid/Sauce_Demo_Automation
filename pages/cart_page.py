from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        print('Opening main page')

    # locators
    checkout_button_loc = 'checkout'

    # getters
    def get_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.checkout_button_loc)))

    # actions
    def open_checkout(self):
        with allure.step("Check out"):
            self.get_checkout().click()
            print('Checking out!')
