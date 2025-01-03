from selenium.webdriver.common.by import By
from locators.checkout_page_locators import CheckoutPageLocators

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart(self):
        self.driver.find_element(*CheckoutPageLocators.ADD_TO_CART).click()

    def select_product_size(self, size_index):
        size_selector = CheckoutPageLocators.PRODUCT_SIZE.format(size_index)
        self.driver.find_element(*size_selector).click()

    def increment_cart_item(self, item_index):
        increment_selector = CheckoutPageLocators.CART_ITEM_INCREMENT.format(item_index)
        self.driver.find_element(*increment_selector).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*CheckoutPageLocators.PROCEED_TO_CHECKOUT).click()

    def select_payment_option(self, option_index):
        payment_option_selector = CheckoutPageLocators.PAYMENT_OPTION.format(option_index)
        self.driver.find_element(*payment_option_selector).click()

    def confirm_order(self):
        self.driver.find_element(*CheckoutPageLocators.CONFIRM_ORDER).click()