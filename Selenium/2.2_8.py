from selenium import webdriver
import os,time
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    first = browser.find_element_by_css_selector('[name="firstname"]')
    first.send_keys("Aleks")

    last = browser.find_element_by_css_selector('[name="lastname"]')
    last.send_keys("B")

    mail = browser.find_element_by_css_selector('[name="email"]')
    mail.send_keys("aa@a.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')


    attach = browser.find_element_by_css_selector('[name="file"]')
    attach.send_keys(file_path)

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