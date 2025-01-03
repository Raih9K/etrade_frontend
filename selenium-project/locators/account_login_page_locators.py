class AccountLoginPageLocators:
    USERNAME_INPUT = (By.NAME, "username")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-bg-primary")
    REGISTER_LINK = (By.LINK_TEXT, "REGISTER HERE.")
    FORGET_PASSWORD_LINK = (By.LINK_TEXT, "Forget password?")
    BACK_BUTTON = (By.CSS_SELECTOR, ".back-btn")