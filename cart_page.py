from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, chrome_driver, firefox_driver):
        self.chrome_driver = chrome_driver
        self.firefox_driver = firefox_driver

    def checkout(self):
        shopping_cart = self.chrome_driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart.click()
        checkout_button = self.chrome_driver.find_element(By.CLASS_NAME, "checkout_button")
        checkout_button.click()
        shopping_cart = self.firefox_driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart.click()
        checkout_button = self.firefox_driver.find_element(By.CLASS_NAME, "checkout_button")
        checkout_button.click()

    def is_cart_empty(self):
        shopping_cart = self.chrome_driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart.click()
        shopping_cart = self.firefox_driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart.click()

        try:
            self.chrome_driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart_item')))
            self.firefox_driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart_item')))
            return False
        except:
            return True
