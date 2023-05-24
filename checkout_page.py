from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CheckoutPage:
    def __init__(self, chrome_driver, firefox_driver):
        self.chrome_driver = chrome_driver
        self.firefox_driver = firefox_driver

    def enter_shipping_info(self, first_name, last_name, zip_code):
        first_name_input = self.chrome_driver.find_element(By.ID, "first-name")
        first_name_input.send_keys(first_name)

        first_name_input = self.firefox_driver.find_element(By.ID, "first-name")
        first_name_input.send_keys(first_name)

        last_name_input = self.chrome_driver.find_element(By.ID, "last-name")
        last_name_input.send_keys(last_name)

        last_name_input = self.firefox_driver.find_element(By.ID, "last-name")
        last_name_input.send_keys(last_name)

        zip_code_input = self.chrome_driver.find_element(By.ID, "postal-code")
        zip_code_input.send_keys(zip_code)

        zip_code_input = self.firefox_driver.find_element(By.ID, "postal-code")
        zip_code_input.send_keys(zip_code)

    def continue_to_summary(self):
        continue_button = self.chrome_driver.find_element(By.ID, "continue")
        continue_button.click()

        continue_button = self.firefox_driver.find_element(By.ID, "continue")
        continue_button.click()

    def finish_checkout(self):
        finish_button = self.chrome_driver.find_element(By.ID, "finish")
        finish_button.click()

        finish_button = self.firefox_driver.find_element(By.ID, "finish")
        finish_button.click()

    def back_to_inventory(self):
        back_button = self.chrome_driver.find_element(By.ID, "back-to-products")
        back_button.click()

        back_button = self.firefox_driver.find_element(By.ID, "back-to-products")
        back_button.click()

    def cancel_order(self):
        cancel_button = self.chrome_driver.find_element(By.ID, "cancel")
        cancel_button.click()

        cancel_button = self.firefox_driver.find_element(By.ID, "cancel")
        cancel_button.click()