from selenium import webdriver
import time
import math

link = "https://suninjuly.github.io/execute_script.html"

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
    input_value = browser.find_element_by_id('input_value')
    x = input_value.text
    return int(x)




if __name__ == '__main__':
    try:
        browser = init(link)
        input_val = calc(get_x(browser))
        answer_input = browser.find_element_by_id('answer')
        answer_input.send_keys(input_val)
        browser.find_element_by_id('robotCheckbox').click()
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        browser.find_element_by_id('robotsRule').click()
        button.click()
        time.sleep(10)
    except Exception as e:
        print(e)
    finally:
        browser.quit()
