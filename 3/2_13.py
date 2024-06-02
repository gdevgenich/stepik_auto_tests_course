from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class Tests(unittest.TestCase):

    def test_first_link(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("First name")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Second name")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("email@email.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertTrue("Congratulations! You have successfully registered!" == welcome_text)

    def test_second_link(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("First name")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Second name")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("email@email.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertTrue("Congratulations! You have successfully registered!" == welcome_text)