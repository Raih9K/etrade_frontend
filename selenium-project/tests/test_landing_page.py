from selenium import webdriver
import pytest
from pages.landing_page import LandingPage

class TestLandingPage:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1536, 864)
        yield
        self.driver.quit()

    def test_landing_page_interactions(self, setup):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        landing_page.click_slider_image()
        landing_page.click_main_slider_area()
        landing_page.navigate_slider_controls()
        landing_page.click_check_it_out()
        landing_page.add_to_cart()
        landing_page.scroll_to_bottom()

    def test_account_login_navigation(self, setup):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        landing_page.click_login_icon()
        landing_page.click_register_here()
        landing_page.fill_login_form()
        landing_page.click_forgot_password()
        landing_page.click_back_button()