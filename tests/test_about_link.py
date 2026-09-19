import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.auth import Auth
from pages.main_page import MainPage

#options
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--guest')


def test_about_link():
    with allure.step("Testing About link"):
        print('Start Testing "About" link')

        # driver stuff
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

        auth = Auth(driver)
        auth.authorization('standard_user', 'secret_sauce')

        main_page = MainPage(driver)
        main_page.select_menu_about()
