from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    calc_value = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(calc_value)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()
    robotRadio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotRadio)
    robotRadio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(30)
    browser.close()
