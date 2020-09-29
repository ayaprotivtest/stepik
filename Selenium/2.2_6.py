from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math,time

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    x = browser.find_element_by_id("input_value").text
    answer = math.log(abs(12*math.sin(int(x))))

    input = browser.find_element_by_class_name("form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true)",input)

    input.send_keys(str(answer))

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()