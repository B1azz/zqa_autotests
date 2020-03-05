from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class LoginPageLocators:
    LOGIN_INPUT_USERNAME = (By.CSS_SELECTOR, "#username")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON_LOGIN = (By.CSS_SELECTOR, "#kc-login")
    LOGO_ICON = (By.CSS_SELECTOR, "div.app-link.header-logo")
    USER_ICON = (By.CSS_SELECTOR, ".user-icon")


class LoginPage(BasePage):
    def login_user(self, username, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_INPUT_USERNAME).send_keys(username)
        self.browser.find_element(*LoginPageLocators.LOGIN_INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_LOGIN).click()
        self.wait_until_is_clickable(*LoginPageLocators.LOGO_ICON, 30)

    def should_be_logo_brand(self):
        assert self.is_element_present(*LoginPageLocators.LOGO_ICON), (
            "Logo is not presented")

    def should_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.USER_ICON), (
            "User icon is not presented, probably unauthorized user")