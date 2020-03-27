import time

import pytest


from src.pages.normdocs.normdocs_main_page import NormDocsMainPage
from src.pages.methodologies.methodologies_main_page import MethodologiesMainPage
from src.pages.specs.specs_main_page import SpecsMainPage
from src.pages.zif_page import go_to_qa
from src.pages.zqa_page import go_to_normdocs, go_to_methodologies, go_to_specs


@pytest.mark.clean
@pytest.mark.normdocs
class TestCleanTypedocs:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_normdocs):
        self.main = NormDocsMainPage(browser, browser.current_url)

    @pytest.mark.xfail(reason='Очистка')
    def test_clean_normdocs1(self):
        while True:
            self.main.delete_this_normdoc('Тест Селениум')
            print('---Удален НД Тест Селениум---')

    @pytest.mark.xfail(reason='Очистка')
    def test_clean_normdocs2(self):
        while True:
            self.main.delete_this_normdoc('Тест Селениум тип')
            print('---Удален НД Тест Селениум тип---')

    @pytest.mark.xfail(reason='Очистка')
    def test_clean_normdocs3(self):
        while True:
            self.main.delete_this_normdoc('Тест Селениум удаление')
            print('---Удален НД Тест Селениум удаление---')

    @pytest.mark.xfail(reason='Очистка')
    def test_clean_normdocs4(self):
        while True:
            time.sleep(3)
            self.main.delete_this_normdoc('Тест Селениум copy')
            print('---Удален НД Тест Селениум copy---')


@pytest.mark.clean
@pytest.mark.methodologies
class TestCleanMethodologies:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_methodologies):
        self.main = MethodologiesMainPage(browser, browser.current_url)

    @pytest.mark.xfail(reason='Очистка')
    def test_clean_methodologies_collections(self):
        while True:
            self.main.delete_collection_by_name('Селениум')
            print('---Удален сборник Селениум---')

    @pytest.mark.xfail(reason='Очистка')
    def test_clean_methodologies_methods1(self):
        while True:
            self.main.delete_method_by_name('Селениум')
            print('---Удалена методика Селениум---')

    @pytest.mark.xfail(reason='Очистка')
    def test_clean_methodologies_methods2(self):
        while True:
            self.main.delete_method_by_name('Селениум создание')
            print('---Удалена методика Селениум создание---')

    @pytest.mark.xfail(reason='Очистка')
    def test_clean_methodologies_methods3(self):
        while True:
            self.main.delete_method_by_name('Селениум удаление')
            print('---Удалена методика Селениум удаление---')


@pytest.mark.clean
@pytest.mark.specs
class TestCleanSpecs:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_methodologies):
        self.main = SpecsMainPage(browser, browser.current_url)

    @pytest.mark.xfail(reason='Очистка')
    def test_clean_specs_collections(self):
        while True:
            self.main.delete_collection_by_name('Селениум')
            print('---Удален сборник Селениум---')
