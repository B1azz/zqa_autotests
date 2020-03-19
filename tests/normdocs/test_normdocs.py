import pytest

from src.pages.base_page import BasePage
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


class TestCreateAndEditNormDocs:
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_polygon, go_to_qa, go_to_normdocs):
        self.main = NormDocsMainPage(browser, browser.current_url)
        self.dialog = NormDocsDialog(browser, browser.current_url)

        self.main.click_add_button()
        self.dialog.input_common_tab('Тест Селениум', 'Селениум', 'Методики испытаний',
                                     '12345', 'Для автотеста',
                                     '19-03-2020 00:00', '19-03-2020 8:00', '19-03-2020 17:00')
        self.dialog.click_save_button()

    @pytest.mark.only
    def test_open_edit_dialog(self):
        """Создание нового НД"""
        self.main.refresh_normdoc_table()
        # self.main.search_normdoc_by_name('Тест Селениум')
        self.main.should_be_this_normdoc_in_table('Тест Селениум')

