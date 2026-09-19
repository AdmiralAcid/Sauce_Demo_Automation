from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base


class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        print('Opening main page')

    # locators
    finish_button_loc = 'finish'

    # getters
    def get_finish_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.finish_button_loc)))

    # actions
    def finish_checkout(self):
        with allure.step("Finish checkout"):
            self.get_finish_button().click()
            print('Going to payment')
