import unittest

from selenium.webdriver.common.by import By

from time import sleep


class LoginPage(unittest.TestCase):
    def __init__(self, chrome_driver, firefox_driver):
        self.chrome_driver = chrome_driver
        self.firefox_driver = firefox_driver

    def load(self):
        self.chrome_driver.get('https://www.saucedemo.com')
        self.firefox_driver.get('https://www.saucedemo.com')

    def login(self, username, password):
        username_input = self.chrome_driver.find_element(By.CSS_SELECTOR, "#user-name")
        username_input.send_keys(username)
        username_input = self.firefox_driver.find_element(By.CSS_SELECTOR, "#user-name")
        username_input.send_keys(username)

        password_input = self.chrome_driver.find_element(By.CSS_SELECTOR, "#password")
        password_input.send_keys(password)
        password_input = self.firefox_driver.find_element(By.CSS_SELECTOR, "#password")
        password_input.send_keys(password)

        login_button = self.chrome_driver.find_element(By.CSS_SELECTOR, ".btn_action")
        login_button.click()

        login_button = self.firefox_driver.find_element(By.CSS_SELECTOR, ".btn_action")
        login_button.click()

    def invalid_login(self, username, password):
        username_input = self.chrome_driver.find_element(By.CSS_SELECTOR, "#user-name")
        username_input.send_keys(username)

        username_input = self.firefox_driver.find_element(By.CSS_SELECTOR, "#user-name")
        username_input.send_keys(username)

        password_input = self.chrome_driver.find_element(By.CSS_SELECTOR, "#password")
        password_input.send_keys(password)

        password_input = self.firefox_driver.find_element(By.CSS_SELECTOR, "#password")
        password_input.send_keys(password)

        login_button = self.chrome_driver.find_element(By.CSS_SELECTOR, ".btn_action")
        login_button.click()

        login_button = self.firefox_driver.find_element(By.CSS_SELECTOR, ".btn_action")
        login_button.click()

        self.chrome_driver.implicitly_wait(5)
        self.firefox_driver.implicitly_wait(5)

        error_message_chrome = self.chrome_driver.find_element(By.CSS_SELECTOR, ".error-message-container.error")
        error_message_firefox = self.firefox_driver.find_element(By.CSS_SELECTOR, ".error-message-container.error")
        error_message = error_message_chrome.text + "|" + error_message_firefox.text
        return error_message