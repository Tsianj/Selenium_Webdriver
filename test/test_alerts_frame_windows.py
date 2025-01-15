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

@scenario('features/alerts_frame_windows.feature', 'Open new tab and close the window')
def test_open_new_tab_and_close():
    pass

@scenario('features/alerts_frame_windows.feature', 'Verify "lorem ipsum" in large modal dialog')
def test_verify_lorem_ipsum_in_large_modal():
    pass

@given('I am on the home page')
def open_home_page(browser):
    browser.get('https://demoqa.com')

@when('I navigate to the "Alerts, Frame & Windows" section')
def navigate_to_alerts_frame_windows(browser):
    browser.find_element(By.XPATH, '//h5[text()="Alerts, Frame & Windows"]').click()

@when('I open a new tab and I close the newly opened tab')
def open_and_close_new_tab(browser):
    browser.find_element(By.XPATH, '//span[text()="Browser Windows"]').click()
    browser.find_element(By.ID, 'tabButton').click()
    browser.switch_to.window(browser.window_handles[1])
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

@then('I verify close the newly opened tab')
def verify_close_new_tab(browser):
    assert len(browser.window_handles) == 1

@when('I access the "Modal dialogs" section')
def open_modal_dialogs_section(browser):
    browser.find_element(By.XPATH, '//span[text()="Modal Dialogs"]').click()
    browser.find_element(By.ID, 'showLargeModal').click()

@then('I should see "lorem ipsum" 4 times in the large modal dialog')
def verify_lorem_ipsum_in_large_modal(browser):
    modal_text = browser.find_element(By.CSS_SELECTOR, '.modal-body').text
    assert modal_text.count('Lorem Ipsum') == 4