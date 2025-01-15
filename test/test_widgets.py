import time
import pytest
import pytest_bdd
from pytest_bdd import parsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, when, then
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@scenario('features/widgets.feature', 'Start progress bar and verify completion')
def test_start_progress_bar_and_verify_completion():
    pass

@given('I am on the home page')
def open_home_page(browser):
    browser.get('https://demoqa.com')

@when('I navigate to the "Widgets" section')
def navigate_to_widgets_section(browser):
    browser.find_element(By.XPATH, '//h5[text()="Widgets"]').click()

@when('I start the progress bar')
def start_progress_bar(browser):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By.CSS_SELECTOR, '.show #item-4 > .text').click()
    browser.find_element(By.ID, 'startStopButton').click()

@then('I should see the reset button when the progress bar reaches 100%')
def verify_progress_bar_completion(browser):
    progress_bar = browser.find_element(By.CSS_SELECTOR, '.progress-bar')
    while progress_bar.get_attribute('aria-valuenow') != '100':
        time.sleep(1)
    assert browser.find_element(By.ID, 'resetButton').is_displayed()


@scenario('features/widgets.feature', 'Navigate to Menu and click on Sub Sub Item 2')
def test_navigate_to_menu_and_click_sub_sub_item_2():
    pass

@when('I navigate through the menu to select "Sub Sub Item 2"')
def open_menu_section(browser):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By.XPATH, '//span[text()="Menu"]').click()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    main_item_2 = browser.find_element(By.XPATH, '//a[text()="Main Item 2"]')
    sub_sub_list = browser.find_element(By.XPATH, '//a[text()="SUB SUB LIST »"]')
    actions = ActionChains(browser)
    time.sleep(2)  # Attendre un peu pour s'assurer que le menu est visible
    actions.move_to_element(main_item_2).perform()
    time.sleep(2)  # Attendre un peu pour s'assurer que le menu est visible
    actions.move_to_element(sub_sub_list).perform()
    time.sleep(2)  # Attendre un peu pour s'assurer que le sous-menu est visible
    browser.find_element(By.XPATH, '//a[text()="Sub Sub Item 2"]').click()

@then('"Sub Sub Item 2" should be displayed as selected')
def verify_sub_sub_item_2_is_clicked(browser):
    sub_sub_item_2 = browser.find_element(By.XPATH, '//a[text()="Sub Sub Item 2"]')
    assert sub_sub_item_2 is not None  # Vérifier que l'élément est présent dans le DOM


@scenario('features/widgets.feature', 'Select various options in the Select Menu')
def test_select_various_options_in_select_menu():
    pass

@when('I configure the select menus with the required options')
def open_select_menu_section(browser):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By.XPATH, '//span[text()="Select Menu"]').click()
    browser.find_element(By.XPATH, '//div[text()="Select Option"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//div[text()="Another root option"]').click()
    browser.find_element(By.XPATH, '//div[text()="Select Title"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//div[text()="Other"]').click()
    select = Select(browser.find_element(By.ID, 'oldSelectMenu'))
    time.sleep(1)
    select.select_by_visible_text('Aqua')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By.XPATH, '//div[text()="Select..."]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//div[text()="Red"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//div[text()="Black"]').click()

@then('I should see the options reflected correctly')
def verify_selected_options(browser):
    selected_value = browser.find_element(By.XPATH, '//div[text()="Another root option"]')
    selected_one = browser.find_element(By.XPATH, '//div[text()="Other"]')
    select = Select(browser.find_element(By.ID, 'oldSelectMenu'))
    selected_old_style = select.first_selected_option 
    assert 'Another root option' in selected_value.text
    assert 'Other' in selected_one.text
    assert selected_old_style.text == 'Aqua'
    assert browser.find_element(By.XPATH, '//div[@id="selectMenuContainer"]/div[7]/div/div/div/div').text == 'Red\nBlack'
     
