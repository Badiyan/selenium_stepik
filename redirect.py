from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def init(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        return browser
    except Exception as e:
        print(e)

def redirecting(browser):
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
    submit_btn = browser.find_element_by_class_name('btn')
    submit_btn.click()

def finalise(browser):
    time.sleep(10)
    browser.quit()

if __name__ == '__main__':
    try:
        browser = init(link)
        submit(browser)
        redirecting(browser)
        number = calc(get_x(browser))
        set_input(browser, number)
        submit(browser)
    except Exception as e:
        print(e)
    finally:
        finalise(browser)