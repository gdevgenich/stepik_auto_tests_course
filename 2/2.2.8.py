from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("first name")
    browser.find_element(By.NAME, "lastname").send_keys("last name")
    browser.find_element(By.NAME, "email").send_keys("email@email.email")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    browser.find_element(By.NAME, "file").send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(30)
    browser.close()
