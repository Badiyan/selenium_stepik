from selenium import webdriver
import time

LINK = "http://suninjuly.github.io/find_xpath_form"

# test values
NAME = 'Ivan'
LAST_NAME = 'Petrov'
CITY = 'Smolensk'
COUNTRY = "Russia"

def fill_form(browser):
    first_name_input = browser.find_element_by_tag_name('input')
    first_name_input.send_keys(NAME)
    last_name_input = browser.find_element_by_name('last_name')
    last_name_input.send_keys(LAST_NAME)
    city_input = browser.find_element_by_class_name('city')
    city_input.send_keys(CITY)
    country_input = browser.find_element_by_id('country')
    country_input.send_keys(COUNTRY)

def click_submit(browser):
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

def run():
    try:
        browser = webdriver.Chrome()
        browser.get(LINK)
        fill_form(browser)
        click_submit(browser)
    finally:
        time.sleep(30)
        browser.quit()

run()