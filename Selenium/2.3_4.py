from selenium import webdriver
import math,time


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    answer = math.log(abs(12 * math.sin(int(x))))

    input = browser.find_element_by_class_name("form-control")
    input.send_keys(str(answer))

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