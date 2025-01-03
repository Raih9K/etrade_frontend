from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from locators.landing_page_locators import LandingPageLocators

class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LandingPageLocators()

    def click_slider_image(self):
        self.driver.find_element(*self.locators.SLIDER_IMAGE).click()

    def click_main_slider_area(self):
        self.driver.find_element(*self.locators.MAIN_SLIDER_AREA).click()

    def click_add_to_cart(self):
        self.driver.find_element(*self.locators.ADD_TO_CART_BUTTON).click()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def navigate_to_checkout(self):
        self.driver.find_element(*self.locators.CHECKOUT_BUTTON).click()