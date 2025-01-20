import time
import pytest
import pytest_bdd
from pytest_bdd import parsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, when, then


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('features/saucedemo.feature', 'Successful login and logout with a valid user')
def test_login_logout():
    pass

@given('I am on the login page')
def open_login_page(browser):
    browser.get('https://www.saucedemo.com')

@when('I authenticate using valid credentials')
def enter_username(browser):
    username_input = browser.find_element(By.ID, 'user-name')
    username_input.send_keys('standard_user')
    password_input = browser.find_element(By.ID, 'password')
    password_input.send_keys('secret_sauce')
    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()

@then('I should be logged into the system')
def verify_logged_in(browser):
    assert browser.find_element(By.ID, 'inventory_container').is_displayed(), "User should be logged in"

@when('I log out of the system')
def log_out(browser):
    menu_button = browser.find_element(By.ID, 'react-burger-menu-btn')
    menu_button.click()
    time.sleep(1)  # Attendre que le menu soit visible
    logout_button = browser.find_element(By.ID, 'logout_sidebar_link')
    logout_button.click()

@then('I should be logged out successfully')
def verify_logged_out(browser):
    assert browser.find_element(By.ID, 'login-button').is_displayed(), "User should be logged out"