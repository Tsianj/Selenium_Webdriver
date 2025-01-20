import time
import pytest
import pytest_bdd
from pytest_bdd import parsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, when, then

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('features/tp_demoqa.feature', 'Select a check box list')
def test_input_field_presence():
    pass

@given('I am on the home page')
def open_home_page(browser):
    browser.get('https://demoqa.com')

@when('I go to the "check box" page')
def check_box_page(browser):
    browser.find_element(By.XPATH, '//h5[text()="Elements"]').click()
    browser.find_element(By.XPATH, '//span[text()="Check Box"]').click()
    browser.find_element(By.CSS_SELECTOR, '.rct-icon-expand-close').click()    
    # Sélectionner tous les éléments sauf "Office" et "Excel file.doc"
    checkboxes = browser.find_elements(By.CSS_SELECTOR, '.rct-checkbox')
    for checkbox in checkboxes:
        label = checkbox.find_element(By.XPATH, './ancestor::label/span[@class="rct-title"]').text
        if label not in ["Office", "Excel File.doc"]:
            input_element = checkbox.find_element(By.XPATH, './preceding-sibling::input')
            if not input_element.is_selected():
                checkbox.click()
    
@then('I verify the check boxes are correctly selected')
def verify_check_boxes(browser):
    checkboxes = browser.find_elements(By.CSS_SELECTOR, '.rct-checkbox')
    for checkbox in checkboxes:
        label = checkbox.find_element(By.XPATH, './ancestor::label/span[@class="rct-title"]').text
        input_element = checkbox.find_element(By.XPATH, './preceding-sibling::input')
        if label in ["Office", "Excel File.doc"]:
            assert not input_element.is_selected(), f'{label} should not be selected'
        else:
            assert input_element.is_selected(), f'{label} should be selected'