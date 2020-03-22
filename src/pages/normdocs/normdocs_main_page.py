from src.pages.base_page import BasePage as BP

from src.locators.normdocs.locators_normdocs_main import NormDocsMainLocators as Main, \
    NormDocsDialogLocators as Dialog
from src.pages.zqa_elements import ZQAToolbar, ZQATable, ZQATab, \
    ZQADropDown, ZQAConfirmDialog, ZQADialog, ZQACalendar, ZQADatePicker, ZQAContentContainer


class NormDocsMainPage(BP):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.BP = BP(browser, browser.current_url)
        self.typedocs_tooolbar = ZQAToolbar(Main.TYPEDOCS_TOOLBAR[1], self.BP)
        self.typedocs_tree = ZQATab(Main.TYPEDOCS_TREE[1], self.BP)

        self.normdocs_toolbar = ZQAToolbar(Main.DOCS_TOOLBAR[1], self.BP)
        self.normdocs_table = ZQATable(Main.DOCS_TABLE[1], self.BP)

        self.drop_down = ZQADropDown('', self.BP)
        self.confirm_dialog = ZQAConfirmDialog('', self.BP)
    # region Типы документов

    def choose_typedoc_by_name(self, text):
        self.typedocs_tree.click_to_tree_tab_by_name(text)
        self.some_wait(timeout=1)

    def should_be_normdoc_is_selected(self, text):
        self.typedocs_tree.should_be_tree_tab_by_name_is_selected(text)

    def search_typedoc_by_drop_down(self, text):
        self.typedocs_tooolbar.click_search_button()
        self.typedocs_tooolbar.click_search_input()
        self.some_wait()
        self.drop_down.select_option_by_text(text)

    def hide_or_show_typedocs_tree(self):
        self.typedocs_tooolbar.click_soft_filter_button()

    def should_be_typedocs_tree_is_hided(self):
        assert self.get_element_attribute(*Main.TYPEDOCS_REGION, 'ng-reflect-visible') == 'false'

    def should_be_typedocs_tree_is_showed(self):
        assert self.get_element_attribute(*Main.TYPEDOCS_REGION, 'ng-reflect-visible') == 'true'
    # endregion

    # region Нормативные документы
    def click_add_button(self):
        self.normdocs_toolbar.click_add_button()
        self.some_wait(timeout=1)

    def edit_this_normdoc(self, name):
        self.normdocs_table.choose_table_line_by_cell_text(name)
        self.normdocs_toolbar.click_edit_button()
        self.some_wait(timeout=1)

    def copy_this_normdoc(self, name):
        self.normdocs_table.choose_table_line_by_cell_text(name)
        self.normdocs_toolbar.click_copy_button()
        self.some_wait(timeout=1)

    def delete_this_normdoc(self, name):
        self.normdocs_table.choose_table_line_by_cell_text(name)
        self.normdocs_toolbar.click_delete_button()
        self.some_wait()
        self.confirm_dialog.click_delete_button()
        self.some_wait(timeout=1)

    def refresh_normdoc_table(self):
        self.normdocs_toolbar.click_refresh_button()
        self.some_wait(timeout=1.5)

    def search_normdoc_by_name(self, name):
        self.normdocs_toolbar.click_search_button()
        self.normdocs_toolbar.click_search_input()
        self.normdocs_toolbar.input_search_text(name)
        self.some_wait()

    def should_be_this_normdoc_in_table(self, normdoc_name):
        self.normdocs_table.should_be_line_with_strip_name(normdoc_name)

    def should_be_this_normdoc_not_in_table(self, normdoc_name):
        self.normdocs_table.should_be_not_line_with_strip_name(normdoc_name)

    # endregion


class NormDocsDialog(BP):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.BP = BP(browser, browser.current_url)
        self.dialog = ZQADialog(Dialog.DIALOG[1], self.BP)
        self.dialog_tabs = ZQATab(Dialog.DIALOG_TREE[1], self.BP)
        self.accept_date = ZQADatePicker(Dialog.ACCEPT_DATE[1], self.BP)
        self.start_date = ZQADatePicker(Dialog.START_DATE[1], self.BP)
        self.stop_date = ZQADatePicker(Dialog.STOP_DATE[1], self.BP)
        self.drop_down = ZQADropDown('', self.BP)
        self.calendar = ZQACalendar('', self.BP)
        self.content = ZQAContentContainer(Dialog.CONTENT_CONTAINER[1], self.BP)

    def should_be_normdocs_dialog(self):
        assert self.is_element_present(*Dialog.DIALOG), 'Диалог создания НД не появился'

    def switch_tab_by_name(self, name):
        self.dialog_tabs.click_to_tree_tab_by_name(name)

    def click_save_button(self):
        self.dialog.click_save_button()
        self.some_wait(timeout=1)

    def click_close_button(self):
        self.dialog.click_close_button()
        self.some_wait(timeout=1)

    # region Общие
    def should_be_in_common_tab(self):
        assert self.is_element_present(*Dialog.NAME), 'Нет поля Наименование'
        assert self.is_element_present(*Dialog.CODE), 'Нет поля Обозначение'
        assert self.is_element_present(*Dialog.TYPEDOC), 'Нет поля Тип нормативного документа'

    def input_name(self, name):
        self.clear_input_text(*Dialog.NAME, name)

    def input_code(self, code):
        self.clear_input_text(*Dialog.CODE, code)

    def choose_typedoc(self, typedoc):
        self.click_to_element(*Dialog.TYPEDOC)
        self.some_wait()
        self.drop_down.select_option_by_text(typedoc)

    def input_order_number(self, number):
        self.clear_input_text(*Dialog.ORDER_NUMBER, number)

    def input_description(self, description):
        self.clear_input_text(*Dialog.DESCRIPTION, description)

    def choose_accept_date(self, year, month, day, time):
        self.accept_date.click_to_calendar()
        self.some_wait()
        self.calendar.choose_date(year, month, day)
        self.accept_date.click_to_time_button()
        self.drop_down.select_menu_line_by_text(time)

    def input_accept_date(self, accept_date):
        self.accept_date.input_text_to_date_input(accept_date)
        self.some_wait()

    def choose_start_date(self, year, month, day, time):
        self.start_date.click_to_calendar()
        self.some_wait()
        self.calendar.choose_date(year, month, day)
        self.start_date.click_to_time_button()
        self.drop_down.select_menu_line_by_text(time)

    def input_start_date(self, start_date):
        self.start_date.input_text_to_date_input(start_date)

    def choose_stop_date(self, year, month, day, time):
        self.stop_date.click_to_calendar()
        self.some_wait()
        self.calendar.choose_date(year, month, day)
        self.stop_date.click_to_time_button()
        self.drop_down.select_menu_line_by_text(time)

    def input_stop_date(self, stop_date):
        self.stop_date.input_text_to_date_input(stop_date)

    def input_common_tab(self, name, code, typedoc, number, description, accept_date, start_date, stop_date):
        self.switch_tab_by_name('Общие')
        if name != '':
            self.input_name(name)
        if code != '':
            self.input_code(code)
        if typedoc != '':
            self.choose_typedoc(typedoc)
        if number != '':
            self.input_order_number(number)
        if description != '':
            self.input_description(description)
        if accept_date != '':
            self.input_accept_date(accept_date)
        if start_date != '':
            self.input_start_date(start_date)
        if stop_date != '':
            self.input_stop_date(stop_date)

    def should_be_in_common_tab_values(self, name, code, typedoc, number, description,
                                       accept_date, start_date, stop_date):
        _name = self.get_element_attribute(*Dialog.NAME, 'value')
        _code = self.get_element_attribute(*Dialog.CODE, 'value')
        _typedoc = self.get_element_attribute(*Dialog.TYPEDOC_INPUT, 'value')
        _number = self.get_element_attribute(*Dialog.ORDER_NUMBER, 'value')
        _description = self.get_element_attribute(*Dialog.DESCRIPTION, 'value')
        assert _name == name
        assert _code == code
        assert _typedoc == typedoc
        assert _number == number
        assert _description == description
        self.accept_date.should_be_in_date_input(accept_date)
        self.start_date.should_be_in_date_input(start_date)
        self.stop_date.should_be_in_date_input(stop_date)
    # endregion

    # region Содержимое
    def click_content_add(self):
        self.click_to_element(*Dialog.CONTENT_TABLE_ADD)
        self.some_wait()

    def click_content_remove(self):
        self.click_to_element(*Dialog.CONTENT_TABLE_REMOVE)
        self.some_wait()

    def click_content_by_name(self, name):
        content_item = self.add_strip_text_to_locator(*Dialog.CONTENT_TABLE_ITEM, name)
        self.click_to_element(*content_item)

    def choose_content_by_name(self, name):
        content_item = self.add_strip_text_to_locator(*Dialog.CONTENT_TABLE_ITEM, name)
        content_item_string = (content_item[0], content_item[1] + "/..")
        if "active" not in self.get_element_attribute(*content_item_string, "class"):
            self.click_to_element(*content_item)

    def input_content_name(self, name):
        self.click_to_element(*Dialog.CONTENT_NAME)
        self.clear_input_text(*Dialog.CONTENT_NAME, name)

    def should_be_content_name(self, name):
        _name = self.get_element_attribute(*Dialog.CONTENT_NAME, 'value')
        assert _name == name

    def add_content(self, name, content_string):
        self.click_content_add()
        self.input_content_name(name)
        self.content.input_to_content_text(content_string)
        self.content.click_to_save_button()
        self.some_wait()

    def remove_content(self, name):
        self.choose_content_by_name(name)
        self.click_content_remove()

    def edit_content(self, name, new_name, content_string):
        self.choose_content_by_name(name)
        self.input_content_name(new_name)
        self.content.input_to_content_text(content_string)
        self.content.click_to_save_button()
        self.some_wait()

    def should_be_content_not_in_table_by_name(self, name):
        content_item = self.add_text_to_locator(*Dialog.CONTENT_TABLE_ITEM, name)
        assert self.is_not_element_present(*content_item)

    def should_be_in_content_fields(self, name, content_string):
        self.choose_content_by_name(name)
        self.should_be_content_name(name)
        self.content.should_be_content_text(content_string)
    # endregion

    # region Положения нормативного документа

    # endregion
