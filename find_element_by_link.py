from selenium import webdriver
import time
import math

# task values
FORMULA = str(math.ceil(math.pow(math.pi, math.e)*10000))

LINK = "http://suninjuly.github.io/find_link_text"

# test values
NAME = 'Ivan'
LAST_NAME = 'Petrov'
CITY = 'Smolensk'
COUNTRY = "Russia"


def fill_form(name,last_name,city,country):
    first_name_input = browser.find_element_by_tag_name('input')
    first_name_input.send_keys(name)
    last_name_input = browser.find_element_by_name('last_name')
    last_name_input.send_keys(last_name)
    city_input = browser.find_element_by_class_name('city')
    city_input.send_keys(city)
    country_input = browser.find_element_by_id('country')
    country_input.send_keys(country)

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    neo_link = browser.find_element_by_link_text(FORMULA)
    neo_link.click()

    fill_form(NAME,
              LAST_NAME,
              CITY,
              COUNTRY)
    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()