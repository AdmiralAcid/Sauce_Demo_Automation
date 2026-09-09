import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from pages.auth import Auth
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfo
from pages.final_page import FinalPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

#options
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--guest')

# driver stuff
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

def test_about_link():
    with allure.step("Testing About link"):
        print('Start Testing "About" link')

        auth = Auth(driver)
        auth.authorization('standard_user', 'secret_sauce')

        main_page = MainPage(driver)
        main_page.select_menu_about()
