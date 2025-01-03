from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_locator):
        self.driver.find_element(*product_locator).click()

    def increase_cart_item_quantity(self, item_locator):
        self.driver.find_element(*item_locator).click()

    def proceed_to_checkout(self, checkout_locator):
        self.driver.find_element(*checkout_locator).click()

    def get_cart_item_count(self, count_locator):
        return self.driver.find_element(*count_locator).text

    def view_cart(self, cart_locator):
        self.driver.find_element(*cart_locator).click()