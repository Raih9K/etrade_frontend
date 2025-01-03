class CheckoutPageLocators:
    PAYMENT_OPTION = (By.CSS_SELECTOR, ".payment-option")
    INPUT_FIELD_NAME = (By.NAME, "name")
    INPUT_FIELD_EMAIL = (By.NAME, "email")
    INPUT_FIELD_ADDRESS = (By.NAME, "address")
    BUTTON_PLACE_ORDER = (By.CSS_SELECTOR, ".place-order-button")
    BUTTON_CANCEL_ORDER = (By.CSS_SELECTOR, ".cancel-order-button")