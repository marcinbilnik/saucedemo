import unittest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


class SauceDemoTest(unittest.TestCase):
    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()

        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)

        self.firefox_options = webdriver.FirefoxOptions()

        self.firefox_driver = webdriver.Firefox(options=self.firefox_options)

    def tearDown(self):
        self.chrome_driver.quit()
        self.firefox_driver.quit()

    def test_wrong_login(self):
        expected_error="Epic sadface: Username and password do not match any user in this service"
        login_page = LoginPage(self.chrome_driver, self.firefox_driver)
        login_page.load()
        error_text=login_page.invalid_login('test', 'test')
        split_text = error_text.split("|")
        chrome = split_text[0]
        firefox = split_text[1]
        self.assertEqual(expected_error, chrome)
        self.assertEqual(expected_error, firefox)


    def test_login_for_locket_user(self):
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        login_page = LoginPage(self.chrome_driver, self.firefox_driver)
        login_page.load()
        error_text=login_page.invalid_login('locked_out_user', 'secret_sauce')
        split_text = error_text.split("|")
        chrome = split_text[0]
        firefox = split_text[1]
        self.assertEqual(expected_error,chrome)
        self.assertEqual(expected_error,firefox)


    def test_cancel_order(self):
        login_page = LoginPage(self.chrome_driver, self.firefox_driver)
        login_page.load()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page = InventoryPage(self.chrome_driver, self.firefox_driver)
        inventory_page.add_by_name_to_cart("Sauce Labs Onesie")
        inventory_page.add_by_name_to_cart("Sauce Labs Fleece Jacket")
        cart_page = CartPage(self.chrome_driver, self.firefox_driver)
        cart_page.checkout()
        checkout_page = CheckoutPage(self.chrome_driver, self.firefox_driver)
        checkout_page.enter_shipping_info('tester', 'test', '12345')
        checkout_page.continue_to_summary()
        checkout_page.cancel_order()

        self.assertEqual(cart_page.is_cart_empty(), False,"Your cart NOT is empty")
        inventory_page.logout()

    def test_add_2_products_to_cart_and_checkout(self):
        login_page = LoginPage(self.chrome_driver, self.firefox_driver)
        login_page.load()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page = InventoryPage(self.chrome_driver, self.firefox_driver)
        inventory_page.add_by_name_to_cart("Sauce Labs Backpack")
        inventory_page.add_by_name_to_cart("Sauce Labs Bike Light")
        cart_page = CartPage(self.chrome_driver, self.firefox_driver)
        cart_page.checkout()
        checkout_page = CheckoutPage(self.chrome_driver, self.firefox_driver)
        checkout_page.enter_shipping_info('tester', 'test', '12345')
        checkout_page.continue_to_summary()
        checkout_page.finish_checkout()
        checkout_page.back_to_inventory()
        inventory_page.logout()

    def test_add_all_to_cart_and_checkout(self):
        login_page = LoginPage(self.chrome_driver, self.firefox_driver)
        login_page.load()
        login_page.login('standard_user','secret_sauce')
        inventory_page = InventoryPage(self.chrome_driver, self.firefox_driver)
        inventory_page.add_to_cart_all()
        cart_page = CartPage(self.chrome_driver, self.firefox_driver)
        cart_page.checkout()
        checkout_page = CheckoutPage(self.chrome_driver, self.firefox_driver)
        checkout_page.enter_shipping_info('tester', 'tester', '12345')
        checkout_page.continue_to_summary()
        checkout_page.finish_checkout()
        checkout_page.back_to_inventory()
        inventory_page.logout()


if __name__ == "__main__":

    unittest.main()
