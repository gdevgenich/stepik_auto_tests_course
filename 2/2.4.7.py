from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "price")))
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.TAG_NAME, "button").click()
    x = browser.find_element(By.ID, "input_value").text
    calc_value = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(calc_value)
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(30)
    browser.close()
