import pytest
from selenium.webdriver.common.by import By

from src.locators.locators_zqa import ZQAPageLocators
from src.pages.base_page import BasePage


@pytest.fixture
def go_to_qa(browser):
    zif = ZifPage(browser, browser.current_url)
    zif.zif_switch_theme()
    zif.zif_go_to_zqa()


class ZifPageLocators:
    BODY = (By.XPATH, "//body[1]")
    LOGO = (By.XPATH, "//img[@class='img-container']")
    # скрыть левое меню
    HIDE_LEFT_MENU_BUTTON = (By.XPATH, "//zps-platform-button[@zpsiconclass='editor-format-indent-decrease']")
    # Сменить локализацию
    SWITCH_LOCALIZATION_BUTTON = (By.XPATH, "//zps-platform-button[@elementclass='app-icon'][2]")
    # Сменить тему
    SWITCH_THEME_BUTTON = (By.XPATH, "//zps-platform-button[@elementclass='app-icon'][1]")
    # Иконка юзера
    USER_ICON_BUTTON = (By.XPATH, "//zps-platform-button[@zpsiconclass='account-circle']")

    # левое меню
    LEFT_MENU = (By.TAG_NAME, "zps-applications-panel")
    # ЛИМС
    Z_QA_LINK = (By.XPATH, "//zps-application-link//h4[text()='Quality Assurance']/../../..")


class ZifPage(BasePage):
    # что должно быть на странице ZIF после логина
    def should_be_zif_page(self):
        assert self.is_element_present(*ZifPageLocators.LOGO), \
            "No logo"
        assert self.is_element_present(*ZifPageLocators.HIDE_LEFT_MENU_BUTTON), \
            "No hide left menu button"
        assert self.is_element_present(*ZifPageLocators.SWITCH_LOCALIZATION_BUTTON), \
            "No switch localization button"
        assert self.is_element_present(*ZifPageLocators.SWITCH_THEME_BUTTON), \
            "No switch theme button"
        assert self.is_element_present(*ZifPageLocators.USER_ICON_BUTTON), \
            "No user icon"
        assert self.is_element_present(*ZifPageLocators.LEFT_MENU), \
            "No left menu"
        assert self.get_element_attribute(*ZifPageLocators.BODY, "class") == "dark-theme", \
            "Dark Theme is not default"
        assert self.get_element_attribute(*ZifPageLocators.LOGO, "alt") == "Logo icon", \
            "Localization is not english"

    # смена локализации
    def zif_switch_localization(self):
        default_value = self.get_element_attribute(*ZifPageLocators.LOGO, "alt")
        self.click_to_element(*ZifPageLocators.SWITCH_LOCALIZATION_BUTTON)
        switch_value = self.get_element_attribute(*ZifPageLocators.LOGO, "alt")
        assert default_value != switch_value, "Localization is not changed"

    # смена темы
    def zif_switch_theme(self):
        default_theme = self.get_element_attribute(*ZifPageLocators.BODY, "class")
        self.click_to_element(*ZifPageLocators.SWITCH_THEME_BUTTON)
        switch_theme = self.get_element_attribute(*ZifPageLocators.BODY, "class")
        assert default_theme != switch_theme, "Theme is not changed"

    # скрыть левое меню
    def zif_hide_left_menu(self):
        assert self.get_element_attribute(*ZifPageLocators.HIDE_LEFT_MENU_BUTTON, "class") \
               == "panel-switcher rotated", "Left menu is hidden now"
        self.click_to_element(*ZifPageLocators.HIDE_LEFT_MENU_BUTTON)
        assert self.get_element_attribute(*ZifPageLocators.HIDE_LEFT_MENU_BUTTON, "class") \
               == "panel-switcher", "Left menu is not hidden now"

    # показать левое меню
    def zif_show_left_menu(self):
        assert self.get_element_attribute(*ZifPageLocators.HIDE_LEFT_MENU_BUTTON, "class") \
               == "panel-switcher", "Left menu is not hidden now"
        self.click_to_element(*ZifPageLocators.HIDE_LEFT_MENU_BUTTON)
        assert self.get_element_attribute(*ZifPageLocators.HIDE_LEFT_MENU_BUTTON, "class") \
               == "panel-switcher rotated", "Left menu is hidden now"

    # проверка, что мы в ЛИМС
    def should_be_to_zqa(self):
        pass

    # переход в ЛИМС
    def zif_go_to_zqa(self):
        self.click_to_element(*ZifPageLocators.Z_QA_LINK)
        self.wait_until_is_clickable(*ZQAPageLocators.ZQA_TITLE, 30)
