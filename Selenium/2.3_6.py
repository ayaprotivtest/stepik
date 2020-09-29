from selenium import webdriver
import math,time


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value.nowrap").text
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