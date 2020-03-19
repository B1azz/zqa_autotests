from src.pages.base_page import BasePage as BP

from src.locators.normdocs.locators_normdocs_main import NormDocsMain as Main, \
    NormDocsDialog as Dialog
from src.pages.zqa_elements import ZQAToolbar, ZQATable, ZQATab, \
    ZQADropDown, ZQAConfirmDialog, ZQADialog


class NormDocsMainPage(BP):
    typedocs_tooolbar = ZQAToolbar(Main.TYPEDOCS_TOOLBAR[1], BP)
    typedocs_tree = ZQATab(Main.TYPEDOCS_TREE[1], BP)

    normdocs_toolbar = ZQAToolbar(Main.DOCS_TOOLBAR[1], BP)
    normdocs_table = ZQATable(Main.DOCS_TABLE[1], BP)

    drop_down = ZQADropDown('', BP)
    confirm_dialog = ZQAConfirmDialog('', BP)
    # region Типы документов

    def choose_typedoc(self, text):
        self.typedocs_tree.click_to_tree_tab_by_name(text)

    def should_be_normdoc_is_selected(self, text):
        self.typedocs_tree.should_be_tree_tab_by_name_is_selected(text)

    def search_typedoc_by_drop_down(self, text):
        self.typedocs_tooolbar.click_search_button()
        self.typedocs_tooolbar.click_search_input()
        self.drop_down.select_option_by_text(text)

    def hide_or_show_typedocs_tree(self):
        self.normdocs_toolbar.click_soft_filter_button()

    def should_be_typedocs_tree_is_hided(self):
        assert self.get_element_attribute(*Main.TYPEDOCS_REGION, 'ng-reflect-visible') == 'false'

    def should_be_typedocs_tree_is_showed(self):
        assert self.get_element_attribute(*Main.TYPEDOCS_REGION, 'ng-reflect-visible') == 'true'
    # endregion

    # region Нормативные документы
    def click_edit_this_normdoc(self, name):
        self.normdocs_table.choose_table_line_by_cell_text(name)
        self.normdocs_toolbar.click_edit_button()

    def copy_this_normdoc(self, name):
        self.normdocs_table.choose_table_line_by_cell_text(name)
        self.normdocs_toolbar.click_copy_button()

    def delete_this_normdoc(self, name):
        self.normdocs_table.choose_table_line_by_cell_text(name)
        self.normdocs_toolbar.click_delete_button()
        self.confirm_dialog.click_delete_button()

    def should_be_this_normdoc_in_table(self, normdoc_name):
        self.normdocs_table.should_be_line_with_name(normdoc_name)
    # endregion


class NormDocsDialog(BP):
    dialog = ZQADialog(*Dialog.DIALOG)
    dialog_tabs = ZQATab(*Dialog.DIALOG_TREE, BP)
    drop_down = ZQADropDown('', BP)

    def should_be_normdocs_dialog(self):
        assert self.is_element_present(*Dialog.DIALOG), 'Диалог создания НД не появился'

    def should_be_in_common_tab(self):
        assert self.is_element_present(*Dialog.NAME), 'Нет поля Наименование'
        assert self.is_element_present(*Dialog.CODE), 'Нет поля Обозначение'
        assert self.is_element_present(*Dialog.TYPEDOC), 'Нет поля Тип нормативного документа'

    def input_name(self, name):
        pass

    def input_code(self, name):
        pass

    def input_order_number(self, name):
        pass
