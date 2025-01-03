from selenium import webdriver
import pytest
from pages.cart_page import CartPage

class TestCartPage:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1536, 864)
        yield
        self.driver.quit()

    def test_add_to_cart(self, setup):
        cart_page = CartPage(self.driver)
        cart_page.open()
        cart_page.add_to_cart()
        assert cart_page.is_item_in_cart()

    def test_increase_cart_item_quantity(self, setup):
        cart_page = CartPage(self.driver)
        cart_page.open()
        cart_page.add_to_cart()
        cart_page.increase_item_quantity()
        assert cart_page.get_cart_item_quantity() == 2

    def test_checkout(self, setup):
        cart_page = CartPage(self.driver)
        cart_page.open()
        cart_page.add_to_cart()
        cart_page.proceed_to_checkout()
        assert cart_page.is_checkout_page_open()