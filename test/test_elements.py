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
    driver.maximize_window()
    yield driver
    driver.quit()

@scenario('features/elements.feature', 'Select a check box list')
def test_input_field_presence():
    pass

@scenario('features/elements.feature', 'Modify web tables')
def test_modify_web_tables():
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

@when('I adjust the web table by removing rows and updating a salary')
def web_tables_page(browser):
    browser.find_element(By.XPATH, '//h5[text()="Elements"]').click()
    browser.find_element(By.XPATH, '//span[text()="Web Tables"]').click()
    browser.find_element(By.ID, 'delete-record-2').click()
    browser.find_element(By.ID, 'delete-record-3').click()
    browser.find_element(By.CSS_SELECTOR, '.rt-tr-group .action-buttons span[title="Edit"]').click()
    salary_input = browser.find_element(By.ID, 'salary')
    salary_input.clear()
    salary_input.send_keys('4300')
    browser.find_element(By.ID, 'submit').click()

@then('the salary of the remaining row should be 4300')
def verify_salary(browser):
    salary_element = browser.find_element(By.XPATH, "//div[@class='rt-td' and text()='4300']")
    assert salary_element is not None, "The salary was not updated to 4300"