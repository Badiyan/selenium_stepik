from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def get_x(browser):
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    return x



if __name__ == '__main__':
    try:

        link = "http://suninjuly.github.io/math.html"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(2)

        number = calc(get_x(browser))
        print(number)


        answer_input = browser.find_element_by_id('answer')
        answer_input.send_keys(number)

        robo_checkbox = browser.find_element_by_id('robotCheckbox')
        robo_checkbox.click()

        robo_rediobtn = browser.find_element_by_id('robotsRule')
        robo_rediobtn.click()

        submit_btn = browser.find_element_by_class_name('btn')
        submit_btn.click()

        time.sleep(10)

    except Exception as e:
        print(e)

    finally:
        browser.quit()