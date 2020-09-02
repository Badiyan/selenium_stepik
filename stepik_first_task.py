from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element_by_tag_name('input')
    first_name_input.send_keys("Ivan")
    last_name_input = browser.find_element_by_name('last_name')
    last_name_input.send_keys("Petrov")
    city_input = browser.find_element_by_class_name('city')
    city_input.send_keys("Smolensk")
    country_input = browser.find_element_by_id('country')
    country_input.send_keys("Russia")
    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


    first_name_input = browser.find_element_by_tag_name('input')
    first_name_input.send_keys("Ivan")
    last_name_input = browser.find_element_by_name('last_name')
    last_name_input.send_keys("Petrov")
    city_input = browser.find_element_by_class_name('city')
    city_input.send_keys("Smolensk")
    country_input = browser.find_element_by_id('country')
    country_input.send_keys("Russia")
    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()


