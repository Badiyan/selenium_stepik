from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

def init(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        return browser
    except Exception as e:
        print(e)

def find_elements(browser):
    firstname = browser.find_element_by_name('firstname')
    name = browser.find_element_by_name('lastname')
    email = browser.find_element_by_name('email')
    return (firstname,name,email)

def fill_fields(tuple):
    for element in tuple:
        element.send_keys("Мой ответ")

def submit(browser):
    submit_btn = browser.find_element_by_class_name('btn')
    submit_btn.click()

def finalise(browser):
    time.sleep(10)
    browser.quit()

def create_empty_file():
    file = open('file.txt', 'w')
    file.close()

def upload_file(browser):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    upload = browser.find_element_by_name('file')
    upload.send_keys(file_path)

if __name__ == '__main__':
    try:
        browser = init(link)
        fill_fields(find_elements(browser))
        create_empty_file()
        upload_file(browser)
        submit(browser)
    except Exception as e:
        print(e)
    finally:
        finalise(browser)

