from src.pages.base_page import BasePage as BP

from src.locators.methodologies.locators_methodologies import MethodologiesMainLocators as Main, \
    MethodsDialogLocators as DialogM, CollectionsDialogLocators as DialogC
from src.pages.zqa_elements import ZQAToolbar, ZQATable, ZQATab, \
    ZQAAddDialog, ZQADialog, ZQAConfirmDialog, ZQADropDown, ZQACodeEditor


class MethodologiesMainPage(BP):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.BP = BP(browser, browser.current_url)
        self.collection_toolbar = ZQAToolbar(Main.COLLECTIONS_TOOLBAR[1], self.BP)
        self.collection_tree = ZQATab(Main.COLLECTIONS_TREE[1], self.BP)
        self.methods_toolbar = ZQAToolbar(Main.METHODS_TOOLBAR[1], self.BP)
        self.methods_table = ZQATable(Main.METHODS_TABLE[1], self.BP)

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

    # region Методики
    def search_method_by_name(self, name):
        self.methods_toolbar.click_search_button()
        self.methods_toolbar.click_search_input()
        self.methods_toolbar.input_search_text(name)
        self.some_wait()

    def click_add_method(self):
        self.methods_toolbar.click_add_button()
        self.some_wait(timeout=1)

    def edit_method_by_name(self, name):
        self.methods_table.choose_table_line_by_cell_text(name)
        self.methods_toolbar.click_edit_button()
        self.some_wait(timeout=1)

    def copy_method_by_name(self, name):
        self.methods_table.choose_table_line_by_cell_text(name)
        self.methods_toolbar.click_copy_button()
        self.some_wait(timeout=1)

    def delete_method_by_name(self, name):
        self.methods_table.choose_table_line_by_cell_text(name)
        self.methods_toolbar.click_delete_button()
        self.some_wait(timeout=1)

    def should_be_this_method_in_table(self, method_name):
        self.methods_table.should_be_line_with_strip_name(method_name)

    def should_be_this_method_not_in_table(self, method_name):
        self.methods_table.should_be_not_line_with_strip_name(method_name)
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
        self.some_wait(timeout=1)

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


class MethodsDialog(BP):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.BP = BP(browser, browser.current_url)
        self.dialog = ZQADialog(DialogM.DIALOG[1], self.BP)
        self.dialog_tabs = ZQATab(DialogM.METHODS_TREE[1], self.BP)
        self.drop_down = ZQADropDown('', self.BP)

        self.product_toolbar = ZQAToolbar(DialogM.PRODUCTS_TOOLBAR[1], self.BP)
        self.product_table = ZQATable(DialogM.PRODUCTS_TABLE[1], self.BP)
        self.product_dialog = ZQAAddDialog(DialogM.PRODUCTS_DIALOG[1], self.BP)

        self.labs_toolbar = ZQAToolbar(DialogM.LABS_TOOLBAR[1], self.BP)
        self.labs_table = ZQATable(DialogM.LABS_TABLE[1], self.BP)
        self.labs_dialog = ZQAAddDialog(DialogM.LABS_DIALOG[1], self.BP)

        self.contexts_toolbar = ZQAToolbar(DialogM.CONTEXTS_TOOLBAR[1], self.BP)
        self.contexts_table = ZQATable(DialogM.CONTEXTS_TABLE[1], self.BP)

        self.tests_toolbar = ZQAToolbar(DialogM.TESTS_TOOLBAR[1], self.BP)
        self.tests_table = ZQATable(DialogM.TESTS_TABLE[1], self.BP)
        self.tests_dialog = ()

        self.code_editor = ZQACodeEditor('', self.BP)

        self.collections_toolbar = ZQAToolbar(DialogM.COLLECTIONS_TOOLBAR[1], self.BP)
        self.collections_table = ZQATable(DialogM.COLLECTIONS_TABLE[1], self.BP)
        self.collections_dialog = ZQAAddDialog(DialogM.COLLECTIONS_DIALOG[1], self.BP)

