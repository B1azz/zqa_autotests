from src.pages.base_page import BasePage as BP

from src.locators.specs.locators_specs import SpecsMainLocatorsLocators as Main, \
    CollectionsDialogPageLocators as DialogC, SpecsDialogLocators as DialogS
from src.pages.zqa_elements import ZQAToolbar, ZQATable, ZQATab, ZQAAddDialog, \
    ZQADialog, ZQAConfirmDialog, ZQADropDown


class SpecsMainPage(BP):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.BP = BP(browser, browser.current_url)
        self.collection_toolbar = ZQAToolbar(Main.COLLECTIONS_TOOLBAR[1], self.BP)
        self.collection_tree = ZQATab(Main.COLLECTIONS_TREE[1], self.BP)
        self.specs_toolbar = ZQAToolbar(Main.SPECS_TOOLBAR[1], self.BP)
        self.specs_table = ZQATable(Main.SPECS_TABLE[1], self.BP)

        self.confirm_dialog = ZQAConfirmDialog('', self.BP)

    # region Сборники
    def choose_collection_by_name(self, text):
        self.collection_tree.click_to_tree_tab_by_name(text)
        self.some_wait(timeout=1)

    def should_be_collection_is_selected(self, text):
        self.collection_tree.should_be_tree_tab_by_name_is_selected(text)

    def search_collection_by_name(self, text):
        self.collection_toolbar.click_search_button()
        self.collection_toolbar.click_search_input()
        self.collection_toolbar.input_search_text(text)
        self.some_wait()

    def hide_collection_tree(self):
        self.collection_toolbar.click_soft_filter_button()

    def should_be_collections_tree_is_hided(self):
        assert self.get_element_attribute(*Main.COLLECTIONS_REGION, 'ng-reflect-visible') == 'false'

    def should_be_collections_tree_is_showed(self):
        assert self.get_element_attribute(*Main.COLLECTIONS_REGION, 'ng-reflect-visible') == 'true'

    def should_be_collection_by_name_in_tree(self, name):
        self.collection_tree.should_be_tree_tab_by_name(name)

    def should_be_not_collection_by_name_in_tree(self, name):
        self.collection_tree.should_be_not_tree_tab_by_name(name)

    def click_add_collection(self):
        self.collection_toolbar.click_add_button()
        self.some_wait(timeout=1)

    def edit_collection_by_name(self, name):
        self.collection_tree.click_to_tree_tab_by_name(name)
        self.collection_toolbar.click_edit_button()
        self.some_wait(timeout=1)

    def copy_collection_by_name(self, name):
        self.collection_tree.click_to_tree_tab_by_name(name)
        self.collection_toolbar.click_copy_button()
        self.some_wait(timeout=1)

    def delete_collection_by_name(self, name):
        self.collection_tree.click_to_tree_tab_by_name(name)
        self.collection_toolbar.click_delete_button()
        self.some_wait(timeout=1)
        self.confirm_dialog.click_delete_button()
    # endregion

    # region Спецификации
    def search_spec_by_name(self, name):
        self.specs_toolbar.click_search_button()
        self.specs_toolbar.click_search_input()
        self.specs_toolbar.input_search_text(name)
        self.some_wait()

    def click_add_spec(self):
        self.specs_toolbar.click_add_button()
        self.some_wait(timeout=1)

    def edit_spec_by_name(self, name):
        self.specs_table.choose_table_line_by_cell_text(name)
        self.specs_toolbar.click_edit_button()
        self.some_wait(timeout=1)

    def copy_spec_by_name(self, name):
        self.specs_table.choose_table_line_by_cell_text(name)
        self.specs_toolbar.click_copy_button()
        self.some_wait(timeout=1)

    def delete_spec_by_name(self, name):
        self.specs_table.choose_table_line_by_cell_text(name)
        self.specs_toolbar.click_delete_button()
        self.some_wait()
        self.confirm_dialog.click_delete_button()
        self.some_wait(timeout=1)

    def should_be_this_spec_in_table(self, spec_name):
        self.specs_table.should_be_line_with_strip_name(spec_name)

    def should_be_this_spec_not_in_table(self, spec_name):
        self.specs_table.should_be_not_line_with_strip_name(spec_name)
    # endregion


class CollectionsDialog(BP):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.BP = BP(browser, browser.current_url)
        self.dialog = ZQADialog(DialogC.DIALOG[1], self.BP)

    def should_be_collection_dialog(self):
        assert self.is_element_present(*DialogC.DIALOG), 'Диалог создания коллекции не появился'

    def click_save_button(self):
        self.dialog.click_save_button()
        self.some_wait(timeout=2)

    def click_close_button(self):
        self.dialog.click_close_button()
        self.some_wait(timeout=1)

    def input_name(self, name):
        self.clear_input_text(*DialogC.NAME, name)

    def input_code(self, code):
        self.clear_input_text(*DialogC.CODE, code)

    def input_description(self, description):
        self.clear_input_text(*DialogC.DESCRIPTION, description)

    def input_collection_values(self, name, code, description):
        if name != '':
            self.input_name(name)
        if code != '':
            self.input_code(code)
        if description != '':
            self.input_description(description)

    def should_be_collections_values(self, name, code, description):
        _name = self.get_element_attribute(*DialogC.NAME, 'value')
        _code = self.get_element_attribute(*DialogC.CODE, 'value')
        _description = self.get_element_attribute(*DialogC.DESCRIPTION, 'value')
        assert _name == name
        assert _code == code
        assert _description == description


class SpecsDialog(BP):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.BP = BP(browser, browser.current_url)
        self.dialog = ZQADialog(DialogS.DIALOG[1], self.BP)
        self.dialog_tabs = ZQATab(DialogS.SPECS_TREE[1], self.BP)
        self.drop_down = ZQADropDown('', self.BP)

        self.products_toolbar = ZQAToolbar(DialogS.PRODUCTS_TOOLBAR[1], self.BP)
        self.products_table = ZQATable(DialogS.PRODUCTS_TABLE[1], self.BP)
        self.products_dialog = ZQAAddDialog(DialogS.PRODUCTS_DIALOG[1], self.BP)

        self.tests_toolbar = ZQAToolbar(DialogS.TESTS_TOOLBAR[1], self.BP)
        self.tests_table = ZQATable(DialogS.TESTS_TABLE[1], self.BP)
        self.tests_dialog = _(DialogS.TESTS_DIALOG[1], self.BP)

        self.norms_toolbar = ZQAToolbar(DialogS.NORMS_TOOLBAR[1], self.BP)
        self.norms_table = ZQATable(DialogS.NORMS_TABLE[1], self.BP)
        self.norms_tabs = ZQATab(DialogS.NORMS_TABS[1], self.BP)
        self.norms_sort_dialog = _(DialogS.NORMS_SORT_DIALOG[1], self.BP)
        self.norms_tests_dialog = _(DialogS.NORMS_TESTS_DIALOG[1], self.BP)

        self.collections_toolbar = ZQAToolbar(DialogS.COLLECTIONS_TOOLBAR[1], self.BP)
        self.collections_table = ZQATable(DialogS.COLLECTIONS_TABLE[1], self.BP)
        self.collections_dialog = ZQAAddDialog(DialogS.COLLECTIONS_DIALOG[1], self.BP)

    def should_be_method_dialog(self):
        assert self.is_element_present(*DialogS.DIALOG), 'Диалог создания спецификации не появился'

    def switch_tab_by_name(self, name):
        self.dialog_tabs.click_to_tree_tab_by_name(name)

    def click_save_button(self):
        self.dialog.click_save_button()
        self.some_wait(timeout=1)

    def click_close_button(self):
        self.dialog.click_close_button()
        self.some_wait(timeout=1)

    def check_active(self):
        self.dialog.click_checker()

    def should_be_check_active_state(self, state: bool):
        self.dialog.should_be_checker_state(state)

    # region Общие
    # endregion

    # region Продукты и лаборатории
    def add_products_by_names(self, *products):
        self.switch_tab_by_name('Продукты')
        self.products_toolbar.click_add_button()
        self.some_wait()
        for product in products:
            self.products_dialog.choose_table_line_by_text(product)
        self.products_dialog.click_select_button()
        self.some_wait()

    def check_product_lab(self, product, lab):
        self.switch_tab_by_name('Продукты')
        pass

    def should_be_check_product_tab(self, product, lab):
        self.switch_tab_by_name('Продукты')
        pass

    def should_be_product_in_table_by_name(self, name):
        self.switch_tab_by_name('Продукты')
        self.products_table.should_be_dialog_cell_with_name(name)

    def delete_product_by_name(self, name):
        self.switch_tab_by_name('Продукты')
        self.products_table.click_to_table_dialog_cell_by_text(name)
        self.products_toolbar.click_delete_button()
        self.some_wait()

    def should_be_not_product_in_table_by_name(self, name):
        self.switch_tab_by_name('Продукты')
        self.products_table.should_be_not_dialog_cell_with_name(name)
    # endregion

    # region Показатели
    # endregion

    # region Нормы продукта
    # endregion

    # region Сборники
    def add_collections_by_names(self, *collections):
        self.switch_tab_by_name('Сборники')
        self.collections_toolbar.click_add_button()
        self.some_wait()
        for collection in collections:
            self.collections_dialog.choose_table_line_by_text(collection)
        self.collections_dialog.click_select_button()
        self.some_wait()

    def should_be_collection_in_table_by_name(self, name):
        self.switch_tab_by_name('Сборники')
        self.collections_table.should_be_dialog_cell_with_name(name)

    def delete_collection_by_name(self, name):
        self.switch_tab_by_name('Сборники')
        self.collections_table.click_to_table_dialog_cell_by_text(name)
        self.collections_toolbar.click_delete_button()
        self.some_wait()

    def should_be_not_collection_in_table_by_name(self, name):
        self.switch_tab_by_name('Сборники')
        self.collections_table.should_be_not_dialog_cell_with_name(name)
    # endregion
