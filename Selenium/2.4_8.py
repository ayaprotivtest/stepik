from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math,time


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button = browser.find_element_by_tag_name("button")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button.click()

    x = browser.find_element_by_css_selector("#input_value.nowrap").text
    answer = math.log(abs(12 * math.sin(int(x))))

    input = browser.find_element_by_class_name("form-control")
    input.send_keys(str(answer))

    button = browser.find_element_by_id("solve")
    button.click()

    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()