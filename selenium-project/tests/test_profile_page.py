from selenium import webdriver
import pytest
from pages.profile_page import ProfilePage

class TestProfilePage:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://new.axilthemes.com/demo/template/etrade/index-1.html")
        self.driver.set_window_size(1536, 864)
        yield
        self.driver.quit()

    def test_view_orders(self, setup):
        profile_page = ProfilePage(self.driver)
        profile_page.navigate_to_account()
        profile_page.view_orders()
        assert profile_page.is_orders_displayed()

    def test_view_downloads(self, setup):
        profile_page = ProfilePage(self.driver)
        profile_page.navigate_to_account()
        profile_page.view_downloads()
        assert profile_page.is_downloads_displayed()

    def test_view_addresses(self, setup):
        profile_page = ProfilePage(self.driver)
        profile_page.navigate_to_account()
        profile_page.view_addresses()
        assert profile_page.is_addresses_displayed()

    def test_view_account_details(self, setup):
        profile_page = ProfilePage(self.driver)
        profile_page.navigate_to_account()
        profile_page.view_account_details()
        assert profile_page.is_account_details_displayed()

    def test_logout(self, setup):
        profile_page = ProfilePage(self.driver)
        profile_page.logout()
        assert profile_page.is_logged_out()