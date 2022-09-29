from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome(ChromeDriverManager().install())

try:
    browser.get(link)
    element = browser.find_element(By.ID, 'input_value')
    x = element.text
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("window.scrollBy(0, 100);")
    input_element = browser.find_element(By.CSS_SELECTOR, 'form input')
    input_element.send_keys(y)
    check_element = browser.find_element(By.CSS_SELECTOR, '.form-check>input')
    check_element.click()
    radio_element = browser.find_element(By.CSS_SELECTOR, 'label[for="robotsRule"]')
    radio_element.click()

    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()