from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome(ChromeDriverManager().install())


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    button_1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_1.click()
    browser.switch_to.window(browser.window_handles[1])
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    # confirm = browser.switch_to.alert
    # confirm.accept()

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    button_2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()