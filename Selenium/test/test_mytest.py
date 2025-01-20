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
    # Assurez-vous que le pilote est installé et configuré correctement
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#1er scénario, je teste la présence des éléments dans ma page
@scenario('features/contact_form.feature', 'Verify the presence of the input field')
def test_input_field_presence():
    pass # Les étapes réelles du test seront exécutées par les implémentations d'étapes ci-dessous

@given('I am on the contact page')
def open_contact_page(browser):
    # Ouvrir la page de contact
    browser.get('https://demoqa.com/automation-practice-form')

@then('I should see the "nom" input field "text"')
def verify_input_field(browser):
    # Vérifier la présence du champ de saisie
    browser.find_element(By.ID, 'firstName').send_keys('John')
    browser.find_element(By.ID, 'lastName').send_keys('Doe')
    browser.find_element(By.ID, 'userEmail').send_keys('johndoe@example.com')
    browser.find_element(By.XPATH, '//label[text()="Male"]').click()
    browser.find_element(By.ID, 'userNumber').send_keys('1234567890')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    browser.find_element(By.ID, 'dateOfBirthInput').click()
    time.sleep(2)
    select_month = Select(browser.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select'))
    select_month.select_by_visible_text('April')
    select_year = Select(browser.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select'))
    select_year.select_by_visible_text('1989')
    browser.find_element(By.XPATH, '//div[text()="17"]').click()

    browser.find_element(By.ID, "subjectsInput").send_keys('Maths')
    browser.find_element(By.ID, "subjectsInput").send_keys('\uE007')
    time.sleep(2)

    browser.find_element(By.XPATH, "//label[.='Music']").click()
    browser.find_element(By.ID, 'currentAddress').send_keys('123 Main Street')
    browser.find_element(By.CSS_SELECTOR, '.css-1gtu0rj-indicatorContainer > .css-19bqh2r').click()
    time.sleep(2)
    browser.find_element(By.ID, 'id=react-select-3-option-0').click()
    # browser.find_element(By.ID, 'city').send_keys('Delhi')
    browser.find_element(By.ID, 'submit').click()