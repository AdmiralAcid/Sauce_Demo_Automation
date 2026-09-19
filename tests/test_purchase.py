import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.auth import Auth
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfo
from pages.final_page import FinalPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from utilities.logger import Logger

#options
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--guest')

@pytest.mark.run(order=3)
@allure.description("Test Backpack Purchase")
def test_backpack_purchase(auto_log):
    print('Start Testing Backpack Purchase')

    # driver stuff
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('standard_user', 'secret_sauce')

    main_page = MainPage(driver)
    main_page.select_backpack()

    cart_page = CartPage(driver)
    cart_page.open_checkout()

    userinfo = CheckoutInfo(driver)
    userinfo.info_filling_in('John', 'Doe', '615516')

    payment = PaymentPage(driver)
    payment.finish_checkout()
    
    final_page = FinalPage(driver)
    final_page.finish()
    Logger.write_url(driver.current_url)

@pytest.mark.run(order=2)
def test_bikelight_purchase(auto_log):
    print('Start Testing Bike Light Purchase')

    # driver stuff
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('standard_user', 'secret_sauce')

    main_page = MainPage(driver)
    main_page.select_bike_light()

    cart_page = CartPage(driver)
    cart_page.open_checkout()

    userinfo = CheckoutInfo(driver)
    userinfo.info_filling_in('John', 'Doe', '615516')

    payment = PaymentPage(driver)
    payment.finish_checkout()

    final_page = FinalPage(driver)
    final_page.finish()
    Logger.write_url(driver.current_url)

@pytest.mark.run(order=1)
def test_jacket_purchase(auto_log):
    print('Start Testing Fleece Jacket Purchase')

    # driver stuff
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('standard_user', 'secret_sauce')

    main_page = MainPage(driver)
    main_page.select_jacket()

    cart_page = CartPage(driver)
    cart_page.open_checkout()

    userinfo = CheckoutInfo(driver)
    userinfo.info_filling_in('John', 'Doe', '615516')

    payment = PaymentPage(driver)
    payment.finish_checkout()

    final_page = FinalPage(driver)
    final_page.finish()
    Logger.write_url(driver.current_url)
