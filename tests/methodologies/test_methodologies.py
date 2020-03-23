import pytest

from src.pages.methodologies.methodologies_main_page import MethodologiesMainPage, CollectionsDialog, MethodsDialog
from src.pages.zif_page import go_to_qa
from src.pages.zqa_page import go_to_methodologies


@pytest.mark.ui
@pytest.mark.methodologies
class TestAddEditCollections:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_methodologies):
        self.main = MethodologiesMainPage(browser, browser.current_url)
        self.collections = CollectionsDialog(browser, browser.current_url)

        self.main.click_add_collection()
        self.collections.input_collection_values('Селениум', 'ЮАЙ', 'Какое то описание')
        self.collections.click_save_button()
        yield
        self.main.delete_collection_by_name('Селениум')

    def test_add_collection(self):
        """Добавить сборник"""
        self.main.should_be_collection_by_name_in_tree('Селениум')

    @pytest.mark.xfail(reason='Z10000018-1005')
    def test_search_collection(self):
        """Найти сборник"""
        self.main.search_collection_by_name('селениум')
        self.main.should_be_collection_by_name_in_tree('Селениум')

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
@pytest.mark.methodologies
class TestDeleteCollections:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_methodologies):
        self.main = MethodologiesMainPage(browser, browser.current_url)
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


@pytest.mark.ui
@pytest.mark.methodologies
class TestDeleteMethods:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_methodologies):
        self.main = MethodologiesMainPage(browser, browser.current_url)
        self.methods = MethodsDialog(browser, browser.current_url)

    def test_delete_method(self):
        """Удаление методики"""
        self.main.click_add_method()
        self.methods.input_common_tab('Селениум удаление', 'Селен0', 'Селениум000', 'Какое то описание', False)
        self.methods.check_active()
        self.methods.click_save_button()

        self.main.delete_method_by_name('Селениум удаление')
        self.main.should_be_this_method_not_in_table('Селениум удаление')


@pytest.mark.ui
@pytest.mark.methodologies
class TestAddEditMethods:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_methodologies):
        self.main = MethodologiesMainPage(browser, browser.current_url)
        self.methods = MethodsDialog(browser, browser.current_url)

        self.main.click_add_method()
        self.methods.input_common_tab('Селениум создание', 'Селен0', 'Селениум000', 'Какое то описание', False)
        self.methods.check_active()
        self.methods.click_save_button()
        yield
        self.main.delete_method_by_name('Селениум создание')

    def test_add_method(self):
        """Создание пустой методики"""
        self.main.should_be_this_method_in_table('Селениум создание')

    def test_common_values(self):
        """Проверка вкладки Общие"""
        self.main.edit_method_by_name('Селениум создание')
        self.methods.should_be_in_common_tab_values('Селениум создание', 'Селен0', 'Селениум000',
                                                    'Какое то описание', False)
        self.methods.click_close_button()

    def test_edit_common(self):
        """Редактирование вкладки Общие"""
        self.main.edit_method_by_name('Селениум создание')
        self.methods.input_common_tab('', 'Селен1', 'Селениум111', 'Какое то еще описание', True)
        self.methods.click_save_button()
        self.main.edit_method_by_name('Селениум создание')
        self.methods.should_be_in_common_tab_values('Селениум создание', 'Селен1', 'Селениум111',
                                                    'Какое то еще описание', True)
        self.methods.click_close_button()

    def test_edit_products(self):
        """Редактирование продуктов"""
        self.main.edit_method_by_name('Селениум создание')
        self.methods.add_products_by_names('Руда', 'Пульпа')
        self.methods.click_save_button()
        self.main.edit_method_by_name('Селениум создание')
        self.methods.should_be_product_in_table_by_name('Руда')
        self.methods.should_be_product_in_table_by_name('Пульпа')
        self.methods.should_be_not_product_in_table_by_name('Другое')
        self.methods.click_close_button()

    def test_edit_labs(self):
        """Редактирование лабораторий"""
        self.main.edit_method_by_name('Селениум создание')
        self.methods.add_labs_by_names('НИИ')
        self.methods.click_save_button()
        self.main.edit_method_by_name('Селениум создание')
        self.methods.should_be_lab_in_table_by_name('НИИ')
        self.methods.should_be_not_lab_in_table_by_name('Металлургическая лаборатория')
        self.methods.click_close_button()

    def test_edit_collections(self):
        """Редактирование сборников"""
        self.main.edit_method_by_name('Селениум создание')
        self.methods.add_collections_by_names('124')
        self.methods.click_save_button()
        self.main.edit_method_by_name('Селениум создание')
        self.methods.should_be_collection_in_table_by_name('124')
        self.methods.should_be_not_collection_in_table_by_name('123')
        self.methods.click_close_button()








