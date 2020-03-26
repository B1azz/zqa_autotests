from src.pages.base_page import BasePage as BP

from src.locators.methodologies.locators_methodologies import MethodologiesMainLocators as Main, \
    MethodsDialogLocators as DialogM, CollectionsDialogLocators as DialogC
from src.pages.zqa_elements import ZQAToolbar, ZQATable, ZQATab, \
    ZQAAddDialog, ZQADialog, ZQAConfirmDialog, ZQADropDown, ZQACodeEditor, ZQATestDialog


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

    def hide_search_input(self):
        self.collection_toolbar.click_search_button()
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
        self.some_wait()
        self.confirm_dialog.click_delete_button()
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


class MethodsDialog(BP):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.BP = BP(browser, browser.current_url)
        self.dialog = ZQADialog(DialogM.DIALOG[1], self.BP)
        self.dialog_tabs = ZQATab(DialogM.METHODS_TREE[1], self.BP)
        self.drop_down = ZQADropDown('', self.BP)

        self.products_toolbar = ZQAToolbar(DialogM.PRODUCTS_TOOLBAR[1], self.BP)
        self.products_table = ZQATable(DialogM.PRODUCTS_TABLE[1], self.BP)
        self.products_dialog = ZQAAddDialog(DialogM.PRODUCTS_DIALOG[1], self.BP)

        self.labs_toolbar = ZQAToolbar(DialogM.LABS_TOOLBAR[1], self.BP)
        self.labs_table = ZQATable(DialogM.LABS_TABLE[1], self.BP)
        self.labs_dialog = ZQAAddDialog(DialogM.LABS_DIALOG[1], self.BP)

        self.contexts_toolbar = ZQAToolbar(DialogM.CONTEXTS_TOOLBAR[1], self.BP)
        self.contexts_table = ZQATable(DialogM.CONTEXTS_TABLE[1], self.BP)

        self.tests_toolbar = ZQAToolbar(DialogM.TESTS_TOOLBAR[1], self.BP)
        self.tests_table = ZQATable(DialogM.TESTS_TABLE[1], self.BP)
        self.tests_analog_dialog = ZQATestDialog(DialogM.DIALOG_ANALOG[1], self.BP)
        self.tests_discrete_dialog = ZQATestDialog(DialogM.DIALOG_DISCRETE[1], self.BP)

        self.code_editor = ZQACodeEditor(DialogM.CALCULATIONS_DIALOG[1], self.BP)

        self.collections_toolbar = ZQAToolbar(DialogM.COLLECTIONS_TOOLBAR[1], self.BP)
        self.collections_table = ZQATable(DialogM.COLLECTIONS_TABLE[1], self.BP)
        self.collections_dialog = ZQAAddDialog(DialogM.COLLECTIONS_DIALOG[1], self.BP)

    def should_be_method_dialog(self):
        assert self.is_element_present(*DialogM.DIALOG), 'Диалог создания методики не появился'

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
    def input_name(self, name):
        self.clear_input_text(*DialogM.NAME, name)

    def input_code(self, code):
        self.clear_input_text(*DialogM.CODE, code)

    def input_official_name(self, official_name):
        self.clear_input_text(*DialogM.FULL_NAME, official_name)

    def input_description(self, description):
        self.clear_input_text(*DialogM.DESCRIPTION, description)

    def check_uncertainty(self):
        self.click_to_element(*DialogM.UNCERTAINTY)

    def input_common_tab(self, name, code, official_name, description, uncertainty: bool):
        self.switch_tab_by_name('Общие')
        if name != '':
            self.input_name(name)
        if code != '':
            self.input_code(code)
        if official_name != '':
            self.input_official_name(official_name)
        if description != '':
            self.input_description(description)
        if uncertainty:
            self.check_uncertainty()

    def should_be_in_common_tab_values(self, name, code, official_name, description, uncertainty: bool):
        _name = self.get_element_attribute(*DialogM.NAME, 'value')
        _code = self.get_element_attribute(*DialogM.CODE, 'value')
        _official_name = self.get_element_attribute(*DialogM.FULL_NAME, 'value')
        _description = self.get_element_attribute(*DialogM.DESCRIPTION, 'value')
        checkbox_state = self.get_element_attribute(*DialogM.UNCERTAINTY, "class")
        if "zyfra_checkbox-checked" in checkbox_state:
            _uncertainty = True
        else:
            _uncertainty = False
        assert _name == name
        assert _code == code
        assert _official_name == official_name
        assert _description == description
        assert _uncertainty == uncertainty
    # endregion

    # region Продукты
    def add_products_by_names(self, *products):
        self.switch_tab_by_name('Продукты')
        self.products_toolbar.click_add_button()
        self.some_wait()
        for product in products:
            self.products_dialog.choose_table_line_by_text(product)
        self.products_dialog.click_select_button()
        self.some_wait()

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

    # region Лаборатории
    def add_labs_by_names(self, *labs):
        self.switch_tab_by_name('Лаборатории')
        self.labs_toolbar.click_add_button()
        self.some_wait()
        for lab in labs:
            self.labs_dialog.choose_table_line_by_text(lab)
        self.labs_dialog.click_select_button()
        self.some_wait()

    def should_be_lab_in_table_by_name(self, name):
        self.switch_tab_by_name('Лаборатории')
        self.labs_table.should_be_dialog_cell_with_name(name)

    def delete_lab_by_name(self, name):
        self.switch_tab_by_name('Лаборатории')
        self.labs_table.click_to_table_dialog_cell_by_text(name)
        self.labs_toolbar.click_delete_button()
        self.some_wait()

    def should_be_not_lab_in_table_by_name(self, name):
        self.switch_tab_by_name('Лаборатории')
        self.labs_table.should_be_not_dialog_cell_with_name(name)
    # endregion

    # region Контексты использования
    def add_context_to_table(self, lab, eq_type, product_group, description):
        self.switch_tab_by_name('Контексты использования')
        self.contexts_toolbar.click_add_button()
        index = self.get_count(*self.contexts_table.table_line_locator)
        if lab != '':
            self.contexts_table.click_to_cell_input_by_coordinates(index, 1)
            self.some_wait()
            self.drop_down.select_option_by_text(lab)
        if eq_type != '':
            self.contexts_table.click_to_cell_input_by_coordinates(index, 2)
            self.some_wait()
            self.drop_down.select_option_by_text(eq_type)
        if product_group != '':
            self.contexts_table.click_to_cell_input_by_coordinates(index, 3)
            self.some_wait()
            self.drop_down.select_option_by_text(product_group)
        if description != '':
            self.contexts_table.click_to_cell_input_by_coordinates(index, 4)
            self.contexts_table.input_text_to_table_cell_by_coordinates(index, 4, description)

    def should_be_context_to_table(self, index, lab, eq_type, product_group, description):
        self.switch_tab_by_name('Контексты использования')
        self.contexts_table.should_be_in_cell_input_by_coordinates(index, 1, lab)
        self.contexts_table.should_be_in_cell_input_by_coordinates(index, 2, eq_type)
        self.contexts_table.should_be_in_cell_input_by_coordinates(index, 3, product_group)
        self.contexts_table.should_be_in_cell_input_by_coordinates(index, 4, description)

    def delete_context_to_table(self, index):
        self.switch_tab_by_name('Контексты использования')
        self.contexts_table.click_to_table_line_by_number(index)
        self.contexts_toolbar.click_delete_button()
        self.some_wait()

    def should_be_lines_in_context_table(self, count):
        _count = self.get_count(*self.contexts_table.table_line_locator)
        assert _count == count, 'Неправильное количество контекстов'
    # endregion

    # region Показатели
    def click_add_analog_test(self):
        self.switch_tab_by_name('Показатели')
        self.tests_toolbar.click_add_button()
        self.some_wait(timeout=1)
        self.drop_down.click_mat_menu_button_by_text('Новый аналоговый показатель')

    def click_add_discrete_test(self):
        self.switch_tab_by_name('Показатели')
        self.tests_toolbar.click_add_button()
        self.some_wait()
        self.drop_down.click_mat_menu_button_by_text('Новый дискретный показатель')

    def click_edit_test_by_name(self, name):
        self.switch_tab_by_name('Показатели')
        self.tests_table.click_to_table_dialog_cell_by_text(name)
        self.tests_toolbar.click_edit_button()

    def click_copy_test_by_name(self, name):
        self.switch_tab_by_name('Показатели')
        self.tests_table.click_to_table_dialog_cell_by_text(name)
        self.tests_toolbar.click_copy_button()

    def click_diapason_test_by_name(self, name):
        self.switch_tab_by_name('Показатели')
        self.tests_table.click_to_table_dialog_cell_by_text(name)
        self.tests_toolbar.click_diapason_button()

    def delete_test_by_name(self, name):
        self.switch_tab_by_name('Показатели')
        self.tests_table.click_to_table_dialog_cell_by_text(name)
        self.tests_toolbar.click_delete_button()

    def should_be_test_by_name(self, name):
        self.switch_tab_by_name('Показатели')
        self.tests_table.should_be_dialog_cell_with_name(name)

    def should_be_not_test_by_name(self, name):
        self.switch_tab_by_name('Показатели')
        self.tests_table.should_be_not_dialog_cell_with_name(name)

    def select_analog_by_name(self, name):
        self.tests_analog_dialog.choose_test_by_name(name)

    def select_discrete_by_name(self, name):
        self.tests_discrete_dialog.choose_test_by_name(name)

    def input_analog_inputs(self, name, code, official_name, description):
        self.tests_analog_dialog.input_test_inputs(name, code, official_name, description)

    def should_be_analog_inputs(self, name, code, official_name, description):
        self.tests_analog_dialog.should_be_test_inputs(name, code, official_name, description)

    def input_discrete_inputs(self, name, code, official_name, description):
        self.tests_discrete_dialog.input_test_inputs(name, code, official_name, description)

    def should_be_discrete_inputs(self, name, code, official_name, description):
        self.tests_discrete_dialog.should_be_test_inputs(name, code, official_name, description)

    def input_analog_units(self, unit_class, unit, digit):
        self.tests_analog_dialog.input_test_analog_units(unit_class, unit, digit)

    def should_be_analog_units(self, unit_class, unit, digit):
        self.tests_analog_dialog.should_be_analog_units(unit_class, unit, digit)

    def choose_discrete_set(self, name):
        self.tests_discrete_dialog.choose_discrete_set_by_name(name)

    def should_be_discrete_set(self, name):
        self.tests_discrete_dialog.should_be_digital_set(name)

    def add_analytic_to_analog_test(self, analytic_type, start, additional, max):
        self.tests_analog_dialog.add_line_to_analytic_table(analytic_type, start, additional, max)

    def should_be_analytic_lines_to_analog_test(self, count):
        self.tests_analog_dialog.should_be_lines_to_analytic_table(count)

    def add_analytic_to_discrete_test(self, analytic_type, start, additional, max):
        self.tests_discrete_dialog.add_line_to_analytic_table(analytic_type, start, additional, max)

    def should_be_analytic_lines_to_discrete_test(self, count):
        self.tests_discrete_dialog.should_be_lines_to_analytic_table(count)

    def delete_analytic_to_analog_test(self, index):
        self.tests_analog_dialog.delete_line_to_analytic_table(index)

    def delete_analytic_to_discrete_test(self, index):
        self.tests_discrete_dialog.delete_line_to_analytic_table(index)

    def click_save_analog_test(self):
        self.tests_analog_dialog.click_save_button()

    def click_close_analog_test(self):
        self.tests_analog_dialog.click_close_button()

    def click_save_discrete_test(self):
        self.tests_discrete_dialog.click_save_button()

    def click_close_discrete_test(self):
        self.tests_discrete_dialog.click_close_button()

    # endregion

    # region Расчеты
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
