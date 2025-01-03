from selenium import webdriver
import pytest
from pages.account_login_page import AccountLoginPage

class TestAccountLoginPage:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://new.axilthemes.com/demo/template/etrade/index-1.html")
        self.driver.set_window_size(1536, 864)
        yield
        self.driver.quit()

    def test_register_and_login(self, setup):
        login_page = AccountLoginPage(self.driver)
        login_page.click_login_icon()
        login_page.click_register_here()
        login_page.fill_registration_form("testuser", "testuser@example.com", "password123")
        login_page.submit_registration()
        login_page.click_sign_in()
        login_page.fill_login_form("testuser@example.com", "password123")
        login_page.submit_login()
        assert login_page.is_logged_in()

    def test_forgot_password(self, setup):
        login_page = AccountLoginPage(self.driver)
        login_page.click_login_icon()
        login_page.click_forgot_password()
        login_page.fill_forgot_password_form("testuser@example.com")
        login_page.submit_forgot_password()
        assert login_page.is_confirmation_message_displayed()