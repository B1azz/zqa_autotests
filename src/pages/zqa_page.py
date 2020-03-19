import pytest

from src.locators.locators_zqa import ZQAPageLocators as L
from src.pages.base_page import BasePage


@pytest.fixture
def go_to_methodologies(browser):
    zqa = ZQAPage(browser, browser.current_url)
    zqa.zqa_go_to_some_feature("НСИ/Методики и методы")


@pytest.fixture
def go_to_normdocs(browser):
    zqa = ZQAPage(browser, browser.current_url)
    zqa.zqa_go_to_some_feature("НСИ/Нормативные документы")


class ZQAPage(BasePage):
    # Раскрыть заданную папку
    def zqa_expand_some_package(self, name):
        expand = L.EXPAND
        locator_with_text = self.add_strip_text_to_locator(*L.TREE_LINK_TEXT, name)
        expand_locator = (locator_with_text[0], locator_with_text[1] + expand)
        self.click_to_element(*expand_locator)
        self.some_wait()

    def zqa_choose_some_feature(self, name):
        locator_with_text = self.add_strip_text_to_locator(*L.TREE_LINK_TEXT, name)
        self.click_to_element(*locator_with_text)
        self.some_wait()

    def zqa_go_to_some_feature(self, path):
        """
        Перейти в нужную фичу ЛИМС
        :param path: Путь до фичи с папками, писать через /
        """
        split_path = path.split('/')
        for i in range(len(split_path) - 1):
            self.zqa_expand_some_package(split_path[i])
        self.zqa_choose_some_feature(split_path[-1])