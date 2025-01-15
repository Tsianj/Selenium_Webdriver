import time
import pytest
import pytest_bdd
from pytest_bdd import parsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, when, then

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@scenario('features/book_store.feature', 'Search for a book by Marijn Haverbeke')
def test_search_for_book_by_marijn_haverbeke():
    pass

@given('I am on the home page')
def open_home_page(browser):
    browser.get('https://demoqa.com')

@when('I navigate to the "Book Store Application" section')
def navigate_to_book_store_application(browser):
    element = browser.find_element(By.XPATH, '//h5[text()="Book Store Application"]')
    browser.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)  # Attendre un peu pour s'assurer que le défilement est terminé
    element.click()

@when('I search for "Marijn Haverbeke" in the book store')
def search_for_marijn_haverbeke(browser):
    browser.find_element(By.XPATH, '//span[text()="Book Store"]').click()
    search_box = browser.find_element(By.ID, 'searchBox')
    search_box.send_keys('Marijn Haverbeke')
    search_box.send_keys(Keys.RETURN)

@then('I should see the book by "Marijn Haverbeke" displayed')
def verify_book_displayed(browser):
    book_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[text()="Eloquent JavaScript, Second Edition"]'))
    )
    assert book_title.is_displayed()