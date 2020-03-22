import pytest

from src.pages.normdocs.normdocs_main_page import NormDocsMainPage, NormDocsDialog
from src.pages.zif_page import go_to_qa
from src.pages.zqa_page import go_to_normdocs


@pytest.mark.ui
@pytest.mark.normdocs
class TestTypedocs:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_normdocs):
        self.main = NormDocsMainPage(browser, browser.current_url)
        self.dialog = NormDocsDialog(browser, browser.current_url)

    def test_search_typedoc(self):
        """Найти тип НД"""
        self.main.search_typedoc_by_drop_down('Методики испытаний')
        self.main.should_be_normdoc_is_selected('Методики испытаний')

    def test_hide_show_typedocs(self):
        """Скрыть дерево типов НД"""
        self.main.hide_or_show_typedocs_tree()
        self.main.should_be_typedocs_tree_is_hided()


@pytest.mark.ui
@pytest.mark.normdocs
class TestCreateAndEditNormDocs:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_normdocs):
        self.main = NormDocsMainPage(browser, browser.current_url)
        self.dialog = NormDocsDialog(browser, browser.current_url)

        self.main.click_add_button()
        self.dialog.input_common_tab('Тест Селениум', 'Селениум', 'Методики испытаний',
                                     '12345', 'Для автотеста',
                                     '19-03-2020 00:00', '19-03-2020 08:00', '19-03-2020 17:00')
        self.dialog.click_save_button()
        self.main.refresh_normdoc_table()
        yield
        self.main.delete_this_normdoc('Тест Селениум')

    def test_open_edit_dialog(self):
        """Создание нового НД"""
        self.main.should_be_this_normdoc_in_table('Тест Селениум')

    def test_edit_common_tab(self):
        """Изменение данных на вкладке Общие"""
        self.main.edit_this_normdoc('Тест Селениум')
        self.dialog.input_common_tab('', 'Селениум новый', 'Методики отбора',
                                     '2222', 'Для автотеста',
                                     '10-03-2020 00:00', '15-03-2020 08:00', '19-12-2020 17:00')
        self.dialog.click_save_button()
        self.main.refresh_normdoc_table()
        self.main.edit_this_normdoc('Тест Селениум')
        self.dialog.should_be_in_common_tab_values('Тест Селениум', 'Селениум новый', 'Методики отбора',
                                                   '2222', 'Для автотеста',
                                                   '10-03-2020 00:00', '15-03-2020 08:00', '19-12-2020 17:00')
        self.dialog.click_close_button()

    def test_copy_normdoc_main(self):
        """Копирование НД, проверка в таблице"""
        self.main.copy_this_normdoc('Тест Селениум')
        self.main.should_be_this_normdoc_in_table('Тест Селениум copy')
        self.main.delete_this_normdoc('Тест Селениум copy')

    def test_copy_normdoc_dialog(self):
        """Копирование НД, проверка вкалдки Общий"""
        self.main.copy_this_normdoc('Тест Селениум')
        self.main.edit_this_normdoc('Тест Селениум copy')
        self.dialog.should_be_in_common_tab_values('Тест Селениум copy', 'Селениум', 'Методики испытаний',
                                                   '12345', 'Для автотеста',
                                                   '19-03-2020 00:00', '19-03-2020 08:00', '19-03-2020 17:00')

    def test_typedoc_valid(self):
        """Проверка, что НД в нужном типе документа"""
        self.main.choose_typedoc_by_name('Методики испытаний')
        self.main.should_be_this_normdoc_in_table('Тест Селениум')

    def test_add_content_in_normdoc_without_save(self):
        self.main.edit_this_normdoc('Тест Селениум')
        self.dialog.switch_tab_by_name('Содержимое')
        self.dialog.add_content('Некий контент', 'Содержимое некого контента')
        self.dialog.should_be_in_content_fields('Некий контент', 'Содержимое некого контента')
        self.dialog.click_close_button()


@pytest.mark.ui
@pytest.mark.normdocs
class TestContentInNormDocs:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_normdocs):
        self.main = NormDocsMainPage(browser, browser.current_url)
        self.dialog = NormDocsDialog(browser, browser.current_url)

        self.main.click_add_button()
        self.dialog.input_common_tab('Тест Селениум', 'Селениум', 'Методики испытаний',
                                     '12345', 'Для автотеста',
                                     '19-03-2020 00:00', '19-03-2020 8:00', '19-03-2020 17:00')
        self.dialog.switch_tab_by_name('Содержимое')
        self.dialog.add_content('Некий контент', 'Содержимое некого контента')
        self.dialog.click_save_button()
        self.main.edit_this_normdoc('Тест Селениум')
        self.dialog.switch_tab_by_name('Содержимое')
        yield
        self.dialog.click_close_button()
        self.main.delete_this_normdoc('Тест Селениум')

    @pytest.mark.xfail(reason="Z10000018-991")
    def test_add_content_in_normdoc_with_save(self):
        """Создание содержимого в НД"""
        self.dialog.should_be_in_content_fields('Некий контент', 'Содержимое некого контента')

    @pytest.mark.xfail(reason="Z10000018-991")
    def test_edit_content_in_norm_doc(self):
        """Изменение содержимого в НД"""
        self.dialog.edit_content('Некий контент', 'Некий новый контент', 'Содержимое некого нового контента')
        self.dialog.click_save_button()
        self.main.edit_this_normdoc('Тест Селениум')
        self.dialog.switch_tab_by_name('Содержимое')
        self.dialog.should_be_in_content_fields('Некий новый контент', 'Содержимое некого нового контента')

    @pytest.mark.xfail(reason="Z10000018-991")
    def test_remove_content_in_norm_doc(self):
        """Удаление содержимого из НД"""
        self.dialog.remove_content('Некий контент')
        self.dialog.click_save_button()
        self.main.edit_this_normdoc('Тест Селениум')
        self.dialog.switch_tab_by_name('Содержимое')
        self.dialog.should_be_content_not_in_table_by_name('Некий контент')


@pytest.mark.ui
@pytest.mark.normdocs
class TestAutoTypeDoc:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_normdocs):
        self.main = NormDocsMainPage(browser, browser.current_url)
        self.dialog = NormDocsDialog(browser, browser.current_url)

        self.main.choose_typedoc_by_name('Методики испытаний')
        self.main.click_add_button()

    def test_typedoc_is_autocomplete(self):
        """Проверка, что тип выставляется сразу при создании НД"""
        self.dialog.should_be_in_common_tab_values('', '', 'Методики испытаний',
                                                   '', '', '', '', '')

    def test_typedoc_is_autocomplete1(self):
        """Проверка содержимого вкладки Общие"""
        self.dialog.input_common_tab('Тест Селениум тип', 'Селениум тип', '',
                                     '12345', 'Для автотеста',
                                     '19-03-2020 00:00', '19-03-2020 08:00', '19-03-2020 17:00')
        self.dialog.click_save_button()
        self.main.refresh_normdoc_table()
        self.main.edit_this_normdoc('Тест Селениум тип')
        self.dialog.should_be_in_common_tab_values('Тест Селениум тип', 'Селениум тип', 'Методики испытаний',
                                                   '12345', 'Для автотеста',
                                                   '19-03-2020 00:00', '19-03-2020 08:00', '19-03-2020 17:00')
        self.dialog.click_close_button()
        self.main.delete_this_normdoc('Тест Селениум тип')


@pytest.mark.ui
@pytest.mark.normdocs
class TestDeleteNormDocs:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_normdocs):
        self.main = NormDocsMainPage(browser, browser.current_url)
        self.dialog = NormDocsDialog(browser, browser.current_url)

        self.main.click_add_button()
        self.dialog.input_common_tab('Тест Селениум удаление', 'Селениум удаление', 'Методики испытаний',
                                     '', '',
                                     '', '', '')
        self.dialog.click_save_button()

    def test_delete_normdoc(self):
        """Удаление НД"""
        self.main.delete_this_normdoc('Тест Селениум удаление')
        self.main.should_be_this_normdoc_not_in_table('Тест Селениум удаление')
