import pytest

from src.pages.specs.specs_main_page import SpecsDialog, SpecsMainPage, CollectionsDialog
from src.pages.zif_page import go_to_qa
from src.pages.zqa_page import go_to_specs


@pytest.mark.ui
@pytest.mark.specs
class TestAddEditCollections:
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_specs):
        self.main = SpecsMainPage(browser, browser.current_url)
        self.collections = CollectionsDialog(browser, browser.current_url)

        self.main.click_add_collection()
        self.collections.input_collection_values('Селениум', 'ЮАЙ', 'Какое то описание')
        self.collections.click_save_button()
        yield
        self.main.delete_collection_by_name('Селениум')

    def test_add_collection(self):
        """Добавить сборник"""
        self.main.should_be_collection_by_name_in_tree('Селениум')

    def test_search_collection(self):
        """Найти сборник"""
        self.main.search_collection_by_name('cелениум')
        self.main.should_be_collection_by_name_in_tree('Селениум')
        self.main.hide_search_input()

    def test_collection_values(self):
        """Значения внутри сборника"""
        self.main.edit_collection_by_name('Селениум')
        self.collections.should_be_collections_values('Селениум', 'ЮАЙ', 'Какое то описание')
        self.collections.click_close_button()

    def test_edit_collection(self):
        """Редактировать сборник"""
        self.main.edit_collection_by_name('Селениум')
        self.collections.input_collection_values('Селениум', 'ЮААААЙ', 'Другое описание')
        self.collections.click_save_button()
        self.main.edit_collection_by_name('Селениум')
        self.collections.should_be_collections_values('Селениум', 'ЮААААЙ', 'Другое описание')
        self.collections.click_close_button()


@pytest.mark.ui
@pytest.mark.specs
class TestDeleteCollections:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_methodologies):
        self.main = SpecsMainPage(browser, browser.current_url)
        self.collections = CollectionsDialog(browser, browser.current_url)

    def test_delete_collection(self):
        """Удалить сборник"""
        self.main.click_add_collection()
        self.collections.input_collection_values('Селениум удаление', 'ЮАЙ', 'Какое то описание')
        self.collections.click_save_button()
        self.main.delete_collection_by_name('Селениум удаление')
        self.main.should_be_not_collection_by_name_in_tree('Селениум удаление')

    def test_hide_show_collection(self):
        """Скрыть дерево сборников"""
        self.main.hide_collection_tree()
        self.main.should_be_collections_tree_is_hided()