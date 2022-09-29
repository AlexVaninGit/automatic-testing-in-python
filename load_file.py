from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os



link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(ChromeDriverManager().install())
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')


try:
    browser.get(link)
    name_element = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    name_element.send_keys('ALex')
    lastname_element = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    lastname_element.send_keys('Vanin')
    email_element = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email_element.send_keys('ALex@yandex.ru')
    file_element = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    file_element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()