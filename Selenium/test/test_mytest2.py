import time
import pytest
import pytest_bdd
from pytest_bdd import parsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@scenario('features/contact_form.feature', 'Verify the presence of the input field')
def test_input_field_presence():
    pass

@given('I am on the contact page')
def open_contact_page(browser):
    browser.get('https://demoqa.com/automation-practice-form')

@when('I fill in the contact form')
def fill_contact_form(browser):
    browser.find_element(By.ID, 'firstName').send_keys('John')
    browser.find_element(By.ID, 'lastName').send_keys('Doe')
    browser.find_element(By.ID, 'userEmail').send_keys('johndoe@example.com')
    browser.find_element(By.XPATH, '//label[text()="Male"]').click()
    browser.find_element(By.ID, 'userNumber').send_keys('1234567890')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(2)
    browser.find_element(By.ID, 'dateOfBirthInput').click()
    time.sleep(2)
    select_month = Select(browser.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select'))
    select_month.select_by_visible_text('April')
    select_year = Select(browser.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select'))
    select_year.select_by_visible_text('1989')
    browser.find_element(By.XPATH, '//div[text()="17"]').click()
    browser.find_element(By.ID, "subjectsInput").send_keys('Maths')
    browser.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//label[.='Music']").click()
    browser.find_element(By.ID, 'currentAddress').send_keys('123 Main Street')
    time.sleep(2)
    wait = WebDriverWait(browser, 10)
    state_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.css-1pahdxg-control')))
    state_dropdown.click()
    option = wait.until(EC.element_to_be_clickable((By.ID, 'react-select-3-option-0')))
    option.click()
    browser.find_element(By.ID, 'submit').click()

@then('I should see the "nom" input field "text"')
def verify_input_field(browser):
    assert browser.find_element(By.ID, 'firstName').get_attribute('value') == 'John'
    assert browser.find_element(By.ID, 'lastName').get_attribute('value') == 'Doe'
    assert browser.find_element(By.ID, 'userEmail').get_attribute('value') == 'johndoe@example.com'
    assert browser.find_element(By.XPATH, '//label[text()="Male"]').is_selected()
    assert browser.find_element(By.ID, 'userNumber').get_attribute('value') == '1234567890'
    assert browser.find_element(By.ID, 'currentAddress').get_attribute('value') == '123 Main Street'