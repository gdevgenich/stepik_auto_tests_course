from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    calc_value = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(calc_value)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(30)
    browser.close()
