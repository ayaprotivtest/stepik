from selenium import webdriver
import math,time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    inp = browser.find_element_by_css_selector('label>span.nowrap[id="input_value"]').text
    y = calc(inp)

    input2 = browser.find_element_by_css_selector("#answer")
    input2.send_keys(y)

    option1 = browser.find_element_by_css_selector('#robotCheckbox')
    option1.click()

    option2 = browser.find_element_by_css_selector('#robotsRule')
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()