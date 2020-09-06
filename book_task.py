from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"

def init(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        return browser
    except Exception as e:
        print(e)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def get_x(browser):
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    return x

def set_input(browser, x):
    answer_input = browser.find_element_by_id('answer')
    answer_input.send_keys(x)

def submit(browser):
    submit_btn = browser.find_element_by_id('solve')
    submit_btn.click()

def book(browser):
    book_btn = browser.find_element_by_id('book')
    book_btn.click()

def finalise(browser):
    time.sleep(10)
    browser.quit()



if __name__ == '__main__':
    try:
        browser = init(link)
        WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
        book(browser)
        number = calc(get_x(browser))
        set_input(browser, number)
        submit(browser)
    finally:
        finalise(browser)


