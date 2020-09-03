from selenium import webdriver

LINK = "http://suninjuly.github.io/registration2.html"

# test values
VALUE = 'Мой ответ'
CLASS_VARS = ['first', 'second', 'third']
bug = 0

def fill_form(browser):
    for var in CLASS_VARS:
        try:
            element = browser.find_element_by_css_selector('.first_block .form-group .{}'.format(var))
            element.send_keys(VALUE)
        except Exception as error:
            print('Бага тут:\n',error)
            global bug
            bug = 1
            exit(1)

def click_submit(browser):
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


def run():
    try:
        browser = webdriver.Chrome()
        browser.get(LINK)
        fill_form(browser)
        click_submit(browser)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        if bug == 0:
            report = 'без ошибок'
        else:
            report = 'с бажинкой'
        print('Тест отработал {}\n'.format(report),'*'*100)
        browser.quit()

if __name__ == '__main__':
    run()