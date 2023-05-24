from selenium.webdriver.common.by import By
from time import sleep

class InventoryPage:

    def __init__(self, chrome_driver, firefox_driver):
        self.chrome_driver = chrome_driver
        self.firefox_driver = firefox_driver

    def add_to_cart_all(self):
        product_elements = self.chrome_driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product_element in product_elements:
            add_to_cart_button = product_element.find_element(By.XPATH,
                                                              ".//button[contains(text(), 'Add to cart')]")
            add_to_cart_button.click()

        product_elements = self.firefox_driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product_element in product_elements:
            add_to_cart_button = product_element.find_element(By.XPATH,
                                                              ".//button[contains(text(), 'Add to cart')]")
            add_to_cart_button.click()

    def logout(self):
        menu_button = self.chrome_driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()

        menu_button = self.firefox_driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        sleep(3)
        logout_button = self.chrome_driver.find_element(By.ID, "logout_sidebar_link")
        logout_button.click()

        logout_button = self.firefox_driver.find_element(By.ID, "logout_sidebar_link")
        logout_button.click()
        sleep(3)

    def add_by_name_to_cart(self,product_name):
        product_element = self.chrome_driver.find_element(By.XPATH,
                                              f"//div[@class='inventory_item_name' and text()='{product_name}']/ancestor::div[@class='inventory_item']")
        add_to_cart_button = product_element.find_element(By.XPATH, ".//button[contains(text(), 'Add to cart')]")
        add_to_cart_button.click()

        product_element = self.firefox_driver.find_element(By.XPATH,
                                                          f"//div[@class='inventory_item_name' and text()='{product_name}']/ancestor::div[@class='inventory_item']")
        add_to_cart_button = product_element.find_element(By.XPATH, ".//button[contains(text(), 'Add to cart')]")
        add_to_cart_button.click()