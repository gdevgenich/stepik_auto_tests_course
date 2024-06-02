from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    summ = int(num1)+int(num2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summ))
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(30)
    browser.close()
