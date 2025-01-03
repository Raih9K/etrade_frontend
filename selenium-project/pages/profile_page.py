from selenium.webdriver.common.by import By
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        self.driver.find_element(*ProfilePageLocators.MY_ACCOUNT).click()

    def click_orders(self):
        self.driver.find_element(*ProfilePageLocators.ORDERS).click()

    def click_downloads(self):
        self.driver.find_element(*ProfilePageLocators.DOWNLOADS).click()

    def click_addresses(self):
        self.driver.find_element(*ProfilePageLocators.ADDRESSES).click()

    def click_account_details(self):
        self.driver.find_element(*ProfilePageLocators.ACCOUNT_DETAILS).click()

    def click_dashboard(self):
        self.driver.find_element(*ProfilePageLocators.DASHBOARD).click()

    def click_logout(self):
        self.driver.find_element(*ProfilePageLocators.LOGOUT).click()

    def view_order(self, order_index):
        order_locator = ProfilePageLocators.ORDER_VIEW.format(order_index)
        self.driver.find_element(*order_locator).click()