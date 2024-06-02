from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    calc_value = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(calc_value)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(30)
    browser.close()
