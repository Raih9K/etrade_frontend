from selenium import webdriver
import pytest
from pages.checkout_page import CheckoutPage

class TestCheckoutPage:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1536, 864)
        yield
        self.driver.quit()

    def test_checkout_process(self, setup):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.navigate_to_checkout()
        checkout_page.select_payment_option()
        checkout_page.submit_order()
        assert checkout_page.is_order_successful()  # Example assertion, modify as needed

    def test_checkout_with_invalid_data(self, setup):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.navigate_to_checkout()
        checkout_page.enter_invalid_payment_info()
        assert checkout_page.is_error_displayed()  # Example assertion, modify as needed