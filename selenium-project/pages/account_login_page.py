from selenium.webdriver.common.by import By
from locators.account_login_page_locators import AccountLoginPageLocators

class AccountLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*AccountLoginPageLocators.USERNAME_FIELD).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(*AccountLoginPageLocators.EMAIL_FIELD).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*AccountLoginPageLocators.PASSWORD_FIELD).send_keys(password)

    def click_register(self):
        self.driver.find_element(*AccountLoginPageLocators.REGISTER_BUTTON).click()

    def click_sign_in(self):
        self.driver.find_element(*AccountLoginPageLocators.SIGN_IN_BUTTON).click()

    def click_forgot_password(self):
        self.driver.find_element(*AccountLoginPageLocators.FORGOT_PASSWORD_LINK).click()