from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class FinalPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print('Opening main page')

    # actions
    def finish(self):
        print(f'current URL is {self.get_url()}')
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()
