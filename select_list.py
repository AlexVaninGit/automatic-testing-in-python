from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time



link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome(ChromeDriverManager().install())

try:
    browser.get(link)
    num1_element = browser.find_element(By.ID, 'num1')
    x = num1_element.text
    num2_element = browser.find_element(By.ID, 'num2')
    y = num2_element.text
    sum = int(x) + int(y)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(sum))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()