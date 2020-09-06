from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)

def get_summ(browser):
    num_1 = browser.find_element_by_id('num1').text
    num_2 = browser.find_element_by_id('num2').text
    summ = int(num_1) + int(num_2)
    return str(summ)

if __name__ == '__main__':
    try:
        select = Select(browser.find_element_by_tag_name("select"))
        select.select_by_value(get_summ(browser))
        submit_btn = browser.find_element_by_class_name('btn')
        submit_btn.click()
    finally:
        time.sleep(10)
        browser.quit()