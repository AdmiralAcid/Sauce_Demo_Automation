import pytest
from exceptiongroup import catch
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.auth import Auth
from pages.main_page import MainPage

# from pages.main_page import MainPage

#options
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--guest')

problem_user_img_src = 'https://www.saucedemo.com/assets/sl-404-Cq1a9k9X.jpg'

def test_standard_user():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('standard_user', 'secret_sauce')

    # let's check current URL as we should be on main page now
    auth.assert_url("https://www.saucedemo.com/inventory.html")

    print('Successful login')

    driver.close()

def test_locked_out_user():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('locked_out_user', 'secret_sauce')

    # check if we've got right error message
    auth.check_error_text('Epic sadface: Sorry, this user has been locked out.')

    print('This user has been locked out')

    driver.close()

def test_problem_user():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('problem_user', 'secret_sauce')

    main_page = MainPage(driver)

    # check if we've got the same image of a bulldog in any shop item card
    image_objs = main_page.get_item_img_objs()
    print(f"Найдено элементов: {len(image_objs)}")
    for obj in image_objs:
        # outer = obj.get_attribute("outerHTML")
        # print(f"outerHTML={outer}")
        assert obj.get_attribute('src') == problem_user_img_src

    print('Problem user login has happened')

    driver.close()

def test_perf_glitch_user():
    expected_url = "https://www.saucedemo.com/inventory.html"
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('performance_glitch_user', 'secret_sauce')

    try:
        wait = WebDriverWait(driver, 8)
        wait.until(lambda _ : driver.current_url == expected_url)
    except TimeoutException:
        assert 0

    print('Performance Glitch User has been successfully logged in after a few seconds of waiting')

    driver.close()

def test_error_user():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('error_user', 'secret_sauce')

    # let's check current URL as we should be on main page now
    auth.assert_url("https://www.saucedemo.com/inventory.html")

    print('Successful login')

    driver.close()

def test_visual_user():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('visual_user', 'secret_sauce')

    # let's check current URL as we should be on main page now
    auth.assert_url("https://www.saucedemo.com/inventory.html")

    print('Successful login')

    driver.close()

def test_empty_user():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('', 'secret_sauce')

    # check if we've got right error message
    auth.check_error_text('Epic sadface: Username is required')

    print("Can't login without username")

    driver.close()

def test_empty_password():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('standard_user', '')

    # check if we've got right error message
    auth.check_error_text('Epic sadface: Password is required')

    print("Can't login without password")

    driver.close()

def test_wrong_login():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('1@1@1', 'secret_sauce')

    # check if we've got right error message
    auth.check_error_text('Epic sadface: Username and password do not match any user in this service')

    print("Can't login with wrong username")

    driver.close()

def test_wrong_password():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('standard_user', '12345!»№;%')

    # check if we've got right error message
    auth.check_error_text('Epic sadface: Username and password do not match any user in this service')

    print("Can't login with wrong password")

    driver.close()

def test_wrong_login_password():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('1@1@1', '12345!»№;%')

    # check if we've got right error message
    auth.check_error_text('Epic sadface: Username and password do not match any user in this service')

    print("Can't login with wrong username and password")

    driver.close()

def test_repeat_input_auth():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.authorization('1@1@1', '12345!»№;%')

    # check if we've got right error message
    auth.check_error_text('Epic sadface: Username and password do not match any user in this service')

    # close error message
    auth.close_err_msg()

    # try again
    auth.authorization('standard_user', 'secret_sauce')

    # let's check current URL as we should be on main page now
    auth.assert_url("https://www.saucedemo.com/inventory.html")

    print('Successful login after an unsuccessful one')

    driver.close()

def test_skip_auth():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    auth = Auth(driver)
    auth.try_to_skip_authorization('https://www.saucedemo.com/inventory.html')

    # check if we are on auth page
    auth.assert_url("https://www.saucedemo.com/")

    # check if we've got right error message
    auth.check_error_text("Epic sadface: You can only access '/inventory.html' when you are logged in.")

    print("Can't skip authorization")

    driver.close()