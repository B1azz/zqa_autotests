from src.locators.locators_elements import ZQADialogLocators as Dialog, \
    ZQAToolbarLocators as Tlbr, \
    ZQATableLocators as Tbl, \
    ZQATabLocators as Tab, \
    ZQADatePickerLocators as Date, \
    ZQAContentContainerLocators as Content, \
    ZQACalendarLocators as Calendar, \
    ZQADropDownLocators as Drop, \
    ZQAConfirmDialogLocators as Confirm, \
    ZQAAddDialogLocators as Add, \
    ZQACodeEditorLocators as Code, \
    ZQATestDialogLocators as Test


class ZQAElement:
    def __init__(self, entry_locator, bp):
        self.entry_locator = entry_locator
        self.bp = bp


class ZQADialog(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)
        self.close_button = (Dialog.CLOSE_BUTTON[0], self.entry_locator + Dialog.CLOSE_BUTTON[1])
        self.cancel_button = (Dialog.CANCEL_BUTTON[0], self.entry_locator + Dialog.CANCEL_BUTTON[1])
        self.save_button = (Dialog.SAVE_BUTTON[0], self.entry_locator + Dialog.SAVE_BUTTON[1])
        self.dialog_header = (Dialog.DIALOG_HEADER[0], self.entry_locator + Dialog.DIALOG_HEADER[1])
        self.checker = (Dialog.CHECKER[0], self.entry_locator + Dialog.CHECKER[1])

    def should_be_header_text(self, text):
        assert self.bp.get_element_text(*self.dialog_header) == text, 'Неправильный заголовок'

    def click_close_button(self):
        self.bp.click_to_element(*self.close_button)
        self.bp.some_wait()

    def click_cancel_button(self):
        self.bp.click_to_element(*self.cancel_button)
        self.bp.some_wait()

    def click_save_button(self):
        self.bp.click_to_element(*self.save_button)
        self.bp.some_wait()

    def click_checker(self):
        self.bp.click_to_element(*self.checker)
        self.bp.some_wait()

    def should_be_checker_state(self, state: bool):
        checkbox_state = self.bp.get_element_attribute(*self.checker, "class")
        if "zyfra_checkbox-checked" in checkbox_state:
            _state = True
        else:
            _state = False
        assert _state == state, 'Неверное состояние чекера'


class ZQAToolbar(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)
        self.filter_button = (Tlbr.FILTER_BUTTON[0], self.entry_locator + Tlbr.FILTER_BUTTON[1])
        self.add_button = (Tlbr.ADD_BUTTON[0], self.entry_locator + Tlbr.ADD_BUTTON[1])
        self.add_dropdown_button = (Tlbr.ADD_DROPDOWN_BUTTON[0], self.entry_locator + Tlbr.ADD_DROPDOWN_BUTTON[1])
        self.edit_button = (Tlbr.EDIT_BUTTON[0], self.entry_locator + Tlbr.EDIT_BUTTON[1])
        self.copy_button = (Tlbr.COPY_BUTTON[0], self.entry_locator + Tlbr.COPY_BUTTON[1])
        self.diapason_button = (Tlbr.DIAPASON_BUTTON[0], self.entry_locator + Tlbr.DIAPASON_BUTTON[1])
        self.delete_button = (Tlbr.DELETE_BUTTON[0], self.entry_locator + Tlbr.DELETE_BUTTON[1])
        self.search_button = (Tlbr.SEARCH_BUTTON[0], self.entry_locator + Tlbr.SEARCH_BUTTON[1])
        self.refresh_button = (Tlbr.REFRESH_BUTTON[0], self.entry_locator + Tlbr.REFRESH_BUTTON[1])
        self.settings_button = (Tlbr.SETTINGS_BUTTON[0], self.entry_locator + Tlbr.SETTINGS_BUTTON[1])
        self.search_input = (Tlbr.SEARCH_INPUT[0], self.entry_locator + Tlbr.SEARCH_INPUT[1])
        self.end_button = (Tlbr.END_BUTTON[0], self.entry_locator + Tlbr.END_BUTTON[1])
        self.down_button = (Tlbr.DOWN_BUTTON[0], self.entry_locator + Tlbr.DOWN_BUTTON[1])
        self.up_button = (Tlbr.UP_BUTTON[0], self.entry_locator + Tlbr.UP_BUTTON[1])
        self.home_button = (Tlbr.HOME_BUTTON[0], self.entry_locator + Tlbr.HOME_BUTTON[1])

    def click_soft_filter_button(self):
        """
        Клик по по кнопке Фильтр
        """
        self.bp.click_to_element(*self.filter_button)

    def click_add_button(self):
        """
        Клик по кнопке Создать
        """
        self.bp.click_to_element(*self.add_button)

    def click_add_drop_down_button(self):
        self.bp.click_to_element(*self.add_dropdown_button)

    def click_edit_button(self):
        """
        Клик по кнопке Редактировать
        """
        self.bp.click_to_element(*self.edit_button)

    def click_copy_button(self):
        """
        Клик по кнопке Копировать
        """
        self.bp.click_to_element(*self.copy_button)

    def click_diapason_button(self):
        """
        Клик по кнопке Диапазоны
        """
        self.bp.click_to_element(*self.diapason_button)

    def click_delete_button(self):
        """
        Клик по кнопке Удалить
        """
        self.bp.click_to_element(*self.delete_button)

    def click_search_button(self):
        """
        Клик по кнопке Поиск
        """
        self.bp.click_to_element(*self.search_button)

    def click_refresh_button(self):
        """
        Клик по кнопке Обновить
        """
        self.bp.click_to_element(*self.refresh_button)

    def click_settings_button(self):
        """
        Клик по кнопке Настройки
        """
        self.bp.click_to_element(*self.settings_button)

    def click_search_input(self):
        """
        Клик по полю ввода для поиска
        """
        self.bp.click_to_element(*self.search_input)

    def input_search_text(self, text):
        """
        Ввод текста
        :param text: текст
        """
        self.bp.input_text(*self.search_input, text)

    def clear_search_text(self):
        """ Очистить текст """
        self.bp.clear_text(*self.search_input)

    def click_end_button(self):
        self.bp.click_to_element(*self.end_button)

    def click_down_button(self):
        self.bp.click_to_element(*self.down_button)

    def click_up_button(self):
        self.bp.click_to_element(*self.up_button)

    def click_home_button(self):
        self.bp.click_to_element(*self.home_button)


class ZQAAddDialog(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)
        self.header = (Add.HEADER[0], self.entry_locator + Add.HEADER[1])
        self.title = (Add.TITLE[0], self.entry_locator + Add.TITLE[1])
        self.toolbar = (Add.TOOLBAR[0], self.entry_locator + Add.TOOLBAR[1])
        self.table = (Add.TABLE[0], self.entry_locator + Add.TABLE[1])
        self.table2 = (Add.TABLE2[0], self.entry_locator + Add.TABLE2[1])
        self.close_button = (Add.CLOSE_BUTTON[0], self.entry_locator + Add.CLOSE_BUTTON[1])
        self.select_button = (Add.SELECT_BUTTON[0], self.entry_locator + Add.SELECT_BUTTON[1])

        self.add_table_main = ZQATable(self.table[1], self.bp)
        self.add_table_add = ZQATable(self.table2[1], self.bp)
        self.add_toolbar = ZQAToolbar(self.toolbar[1], self.bp)

    def should_be_header_text(self, text):
        _text = self.bp.get_element_text(*self.header)
        assert _text == text

    def input_title(self, text):
        self.bp.clear_input_text(*self.title, text)

    def click_close_button(self):
        self.bp.click_to_element(*self.close_button)

    def click_select_button(self):
        self.bp.click_to_element(*self.select_button)

    def choose_table_line_by_text(self, text, table='main'):
        if table == 'main':
            self.add_table_main.click_to_table_dialog_cell_by_text(text)
        if table == 'add':
            self.add_table_add.click_to_table_dialog_cell_by_text(text)

    def check_table_cell_by_text(self, text, table='main'):
        if table == 'main':
            self.add_table_main.click_to_checker_in_cell_by_text(text)
        if table == 'add':
            self.add_table_main.click_to_checker_in_cell_by_text(text)

    def expand_table_line_by_text(self, text, table='main'):
        if table == 'main':
            self.add_table_main.click_to_expand_in_cell_by_text(text)
        if table == 'add':
            self.add_table_add.click_to_expand_in_cell_by_text(text)

    def input_search_text(self, text):
        self.add_toolbar.input_search_text(text)

    def click_add_button(self):
        self.add_toolbar.click_add_button()

    def click_delete_button(self):
        self.add_toolbar.click_delete_button()

    def click_end_button(self):
        self.add_toolbar.click_end_button()

    def click_down_button(self):
        self.add_toolbar.click_down_button()

    def click_up_button(self):
        self.add_toolbar.click_up_button()

    def click_home_button(self):
        self.add_toolbar.click_home_button()


class ZQATestDialog(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)
        self.close_button = (Test.CLOSE_BUTTON[0], self.entry_locator + Test.CLOSE_BUTTON[1])
        self.cancel_button = (Test.CANCEL_BUTTON[0], self.entry_locator + Test.CANCEL_BUTTON[1])
        self.save_button = (Test.SAVE_BUTTON[0], self.entry_locator + Test.SAVE_BUTTON[1])
        self.header = (Test.HEADER[0], self.entry_locator + Test.HEADER[1])
        self.dialog_inputs = (Test.DIALOG_INPUTS[0], self.entry_locator + Test.DIALOG_INPUTS[1])
        self.name_select = (Test.NAME_SELECT[0], self.entry_locator + Test.NAME_SELECT[1])
        self.name_input = (Test.NAME_INPUT[0], self.entry_locator + Test.NAME_INPUT[1])
        self.code = (Test.CODE[0], self.entry_locator + Test.CODE[1])
        self.official_name = (Test.OFFICIAL_NAME[0], self.entry_locator + Test.OFFICIAL_NAME[1])
        self.description = (Test.DESCRIPTION[0], self.entry_locator + Test.DESCRIPTION[1])

        self.tabs = (Test.TABS[0], self.entry_locator + Test.TABS[1])
        self.common_tab = (Test.COMMON_TAB[0], self.entry_locator + Test.COMMON_TAB[1])
        self.analytic_tab = (Test.ANALYTICS_TAB[0], self.entry_locator + Test.ANALYTICS_TAB[1])

        self.unit_classes = (Test.UNIT_CLASSES[0], self.entry_locator + Test.UNIT_CLASSES[1])
        self.unit_classes_input = (Test.UNIT_CLASSES_INPUT[0], self.entry_locator + Test.UNIT_CLASSES_INPUT[1])
        self.units = (Test.UNITS[0], self.entry_locator + Test.UNITS[1])
        self.units_input = (Test.UNITS_INPUT[0], self.entry_locator + Test.UNITS_INPUT[1])
        self.unit_digits = (Test.UNIT_DIGITS[0], self.entry_locator + Test.UNIT_DIGITS[1])
        self.digital_sets = (Test.DIGITAL_SETS[0], self.entry_locator + Test.DIGITAL_SETS[1])
        self.digital_sets_input = (Test.DIGITAL_SETS_INPUT[0], self.entry_locator + Test.DIGITAL_SETS_INPUT[1])

        self.analytic_table = (Test.ANALYTICS_TABLE[0], self.entry_locator + Test.ANALYTICS_TABLE[1])

        self.drop_down = ZQADropDown('', self.bp)
        self.table = ZQATable(self.analytic_table[1], self.bp)

    def click_close_button(self):
        self.bp.click_to_element(*self.close_button)
        self.bp.some_wait()

    def click_cancel_button(self):
        self.bp.click_to_element(*self.cancel_button)
        self.bp.some_wait()

    def click_save_button(self):
        self.bp.click_to_element(*self.save_button)
        self.bp.some_wait()

    def should_be_header_text(self, text):
        assert self.bp.get_element_text(*self.header) == text, 'Неправильный заголовок'

    def select_test_name_by_name(self, name):
        self.bp.click_to_element(*self.name_select)
        self.drop_down.select_option_by_text(name)

    def input_test_name(self, name):
        self.bp.clear_input_text(*self.name_input, name)

    def input_test_code(self, code):
        self.bp.clear_input_text(*self.code, code)

    def input_test_official_name(self, official_name):
        self.bp.clear_input_text(*self.official_name, official_name)

    def input_test_description(self, description):
        self.bp.clear_input_text(*self.description, description)

    def click_test_name_select(self):
        self.bp.click_to_element(*self.name_select)

    def input_test_inputs(self, name, code, official_name, description):
        if name != '':
            self.input_test_name(name)
        if code != '':
            self.input_test_code(code)
        if official_name != '':
            self.input_test_official_name(official_name)
        if description != '':
            self.input_test_description(description)

    def choose_test_by_name(self, name):
        self.click_test_name_select()
        self.bp.some_wait()
        self.drop_down.select_option_by_text(name)
        self.bp.some_wait()

    def should_be_test_inputs(self, name, code, official_name, description):
        _name = self.bp.get_element_attribute(*self.name_input, 'value')
        _code = self.bp.get_element_attribute(*self.code, 'value')
        _official_name = self.bp.get_element_attribute(*self.official_name, 'value')
        _description = self.bp.get_element_attribute(*self.description, 'value')
        assert _name == name
        assert _code == code
        assert _official_name == official_name
        assert _description == description

    def go_to_common_tab(self):
        self.bp.click_to_element(*self.common_tab)
        self.bp.some_wait()

    def go_to_analytic_tab(self):
        self.bp.click_to_element(*self.analytic_tab)
        self.bp.some_wait()

    def choose_unit_class_by_name(self, name):
        self.bp.click_to_element(*self.unit_classes)
        self.bp.some_wait()
        self.drop_down.select_option_by_text(name)

    def choose_unit_by_name(self, name):
        self.bp.click_to_element(*self.units)
        self.bp.some_wait()
        self.drop_down.select_option_by_text(name)

    def input_unit_digit(self, digit):
        self.bp.click_to_element(*self.unit_digits)
        self.bp.clear_input_text(*self.unit_digits, digit)

    def input_test_analog_units(self, unit_class, unit, digit):
        self.go_to_common_tab()
        if unit_class != '':
            self.choose_unit_class_by_name(unit_class)
        if unit != '':
            self.choose_unit_by_name(unit)
        if digit != '':
            self.input_unit_digit(digit)

    def should_be_analog_units(self, unit_class, unit, digit):
        self.go_to_common_tab()
        _units_class = self.bp.get_element_attribute(*self.unit_classes_input, 'value')
        _unit = self.bp.get_element_attribute(*self.units_input, 'value')
        _digit = self.bp.get_element_attribute(*self.unit_digits, 'value')
        assert _units_class == unit_class
        assert _unit == unit
        assert _digit == digit

    def choose_discrete_set_by_name(self, name):
        self.go_to_common_tab()
        self.bp.click_to_element(*self.digital_sets)
        self.bp.some_wait()
        self.drop_down.select_option_by_text(name)

    def should_be_digital_set(self, name):
        self.go_to_common_tab()
        _name = self.bp.get_element_attribute(*self.digital_sets_input, 'value')
        assert _name == name

    def add_line_to_analytic_table(self, analytic_type, start, additional, max):
        self.go_to_analytic_tab()
        self.table.click_to_table_column_by_number(5)
        index = self.bp.get_count(*self.table.table_line_locator)
        if analytic_type != '':
            self.table.click_to_cell_by_coordinates(index, 1)
            self.bp.some_wait()
            self.drop_down.select_option_by_text(analytic_type)
        if start != '':
            self.table.input_text_to_table_cell_by_coordinates(index, 2, start)
        if additional != '':
            self.table.input_text_to_table_cell_by_coordinates(index, 3, additional)
        if max != '':
            self.table.input_text_to_table_cell_by_coordinates(index, 4, max)

    def edit_line_to_analytic_table(self, tr, analytic_type, start, additional, max):
        self.go_to_analytic_tab()
        if analytic_type != '':
            self.table.click_to_cell_by_coordinates(tr, 1)
            self.bp.some_wait()
            self.drop_down.select_option_by_text(analytic_type)
        if start != '':
            self.table.input_text_to_table_cell_by_coordinates(tr, 2, start)
        if additional != '':
            self.table.input_text_to_table_cell_by_coordinates(tr, 3, additional)
        if max != '':
            self.table.input_text_to_table_cell_by_coordinates(tr, 4, max)

    def delete_line_to_analytic_table(self, tr):
        self.go_to_analytic_tab()
        self.table.click_to_cell_by_coordinates(tr, 5)
        self.bp.some_wait()

    def should_be_lines_to_analytic_table(self, count):
        self.go_to_analytic_tab()
        _count = self.bp.get_count(*self.table.table_line_locator)
        assert _count == count


class ZQACodeEditor(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)
        self.cancel_button = (Code.CANCEL_BUTTON[0], self.entry_locator + Code.CANCEL_BUTTON[1])
        self.save_button = (Code.SAVE_BUTTON[0], self.entry_locator + Code.SAVE_BUTTON[1])
        self.header = (Code.HEADER[0], self.entry_locator + Code.HEADER[1])

    def click_cancel_button(self):
        self.bp.click_to_element(*self.cancel_button)
        self.bp.some_wait()

    def click_save_button(self):
        self.bp.click_to_element(*self.save_button)
        self.bp.some_wait()

    def should_be_header_text(self, text):
        assert self.bp.get_element_text(*self.header) == text, 'Неправильный заголовок'


class ZQATable(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)
        self.text_locator = (Tbl.TEXT[0], self.entry_locator + Tbl.TEXT[1])
        self.column_locator = (Tbl.BUTTON[0], self.entry_locator + Tbl.BUTTON[1])
        self.cell_locator = (Tbl.CELL[0], self.entry_locator + Tbl.CELL[1])
        self.table_line_locator = (Tbl.BLINE[0], self.entry_locator + Tbl.BLINE[1])
        self.dialog_cell = (Tbl.DIALOG_CELL[0], self.entry_locator + Tbl.DIALOG_CELL[1])
        self.cell_checker = (Tbl.CELL_CHECKER[0], self.entry_locator + Tbl.CELL_CHECKER[1])
        self.expand_cell = (Tbl.EXPAND_CELL[0], self.entry_locator + Tbl.EXPAND_CELL[1])

    def click_to_table_dialog_cell_by_text(self, text):
        cell = self.bp.add_text_to_locator(*self.dialog_cell, text)
        line = (cell[0], cell[1]+"/..")
        self.bp.click_to_element(*line)

    def click_to_table_column_by_name(self, name):
        """
        Клик по наименованию столбца таблицы
        :param name: наименование столбца
        """
        column = self.bp.add_text_to_locator(*self.column_locator, name)
        self.bp.click_to_element(*column)

    def click_to_table_column_by_number(self, number):
        """
        Клик по наименованию столбца таблицы
        :param number: номер столбца
        """
        column = self.bp.add_index_to_locator(*self.column_locator, number)
        self.bp.click_to_element(*column)

    def click_to_cell_input_by_coordinates(self, tr, td):
        cell = (self.table_line_locator[0], f"{self.table_line_locator[1]}[{tr}]//td[{td}]//input")
        self.bp.click_to_element(*cell)

    def should_be_in_cell_input_by_coordinates(self, tr, td, text):
        cell = (self.table_line_locator[0], f"{self.table_line_locator[1]}[{tr}]//td[{td}]//input")
        _text = self.bp.get_element_attribute(*cell, 'value')
        assert _text == text

    def click_to_cell_by_coordinates(self, tr, td):
        """
        Клик по ячейке таблице с заданными коордитанами
        :param tr: № строки
        :param td: № столбца
        """
        cell = (self.table_line_locator[0], f"{self.table_line_locator[1]}[{tr}]//td[{td}]")
        self.bp.click_to_element(*cell)

    def input_text_to_table_cell_by_coordinates(self, tr, td, text):
        """
        Ввод текста в ячейку с заданными координатами
        :param tr: № строки
        :param td: № столбца
        :param text: текст
        """
        cell = (self.table_line_locator[0], f"{self.table_line_locator[1]}[{tr}]//td[{td}]//input")
        self.bp.clear_input_text(*cell, text)

    def click_to_table_line_by_cell_text(self, text):
        """
        Клик по ячейке таблицы с тектом
        :param text: текст в ячейке
        """
        cell_by_text = self.bp.add_strip_text_to_locator(*self.cell_locator, text)
        self.bp.click_to_element(*cell_by_text)

    def click_to_table_line_by_number(self, number):
        """
        Клик по строке по порядковому номеру в таблице
        :param number: номер строки
        """
        table_line = self.bp.add_index_to_locator(*self.table_line_locator, number)
        self.bp.click_to_element(*table_line)

    def choose_table_line_by_cell_text(self, text):
        """
        Выбор строки по тексту ячейки внутри, с проверкой
        :param text: текст в ячейке
        """
        cell_by_text = self.bp.add_strip_text_to_locator(*self.cell_locator, text)
        table_line = (cell_by_text[0], cell_by_text[1] + "/../..")
        if "active" not in self.bp.get_element_attribute(*table_line, "class"):
            self.bp.click_to_element(*cell_by_text)

    def choose_table_line_by_cell_text1(self, text):
        """
        Выбор строки по тексту ячейки внутри, с проверкой
        :param text: текст в ячейке c пробелами
        """
        cell_by_text = self.bp.add_text_to_locator(*self.cell_locator, text)
        table_line = (cell_by_text[0], cell_by_text[1] + "/../..")
        if "active" not in self.bp.get_element_attribute(*table_line, "class"):
            self.bp.click_to_element(*cell_by_text)

    def choose_table_line_by_number(self, number):
        """
        Выбор строки по порядковому номеру в таблице, с проверкой
        :param number: номер строки
        """
        table_line = self.bp.add_index_to_locator(*self.table_line_locator, number)
        if "active" not in self.bp.get_element_attribute(*table_line, "class"):
            self.bp.click_to_element(*table_line)

    def should_be_dialog_cell_with_name(self, name):
        cell = self.bp.add_text_to_locator(*self.dialog_cell, name)
        self.bp.is_element_present(*cell)

    def should_be_not_dialog_cell_with_name(self, name):
        cell = self.bp.add_text_to_locator(*self.dialog_cell, name)
        self.bp.is_not_element_present(*cell, timeout=1.5)

    def should_be_line_with_name(self, name):
        cell = self.bp.add_text_to_locator(*self.cell_locator, name)
        table_line = (cell[0], cell[1] + "/../..")
        assert self.bp.is_element_present(*table_line), 'Строки с такой ячейкой нет'

    def should_be_line_with_strip_name(self, name):
        cell = self.bp.add_strip_text_to_locator(*self.cell_locator, name)
        table_line = (cell[0], cell[1] + "/../..")
        assert self.bp.is_element_present(*table_line), 'Строки с такой ячейкой нет'

    def should_be_not_line_with_strip_name(self, name):
        cell = self.bp.add_strip_text_to_locator(*self.cell_locator, name)
        table_line = (cell[0], cell[1] + "/../..")
        assert self.bp.is_not_element_present(*table_line), 'Строка с такой ячейкой в таблице'

    def click_to_checker_in_cell_by_text(self, text):
        cell = self.bp.add_strip_text_to_locator(*self.cell_checker, text)
        checker = (cell[0], cell[1] + "/..")
        self.bp.click_to_element(*checker)

    def should_be_checked_cell_by_text(self, text):
        cell = self.bp.add_strip_text_to_locator(*self.cell_checker, text)
        checker = (cell[0], cell[1] + "/..")
        assert self.bp.get_element_attribute(*checker, 'class') == 'zyfra_container-checkbox zyfra_checkbox-checked'

    def should_be_not_checked_cell_by_text(self, text):
        cell = self.bp.add_strip_text_to_locator(*self.cell_checker, text)
        checker = (cell[0], cell[1] + "/..")
        assert self.bp.get_element_attribute(*checker, 'class') == 'zyfra_container-checkbox'

    def click_to_expand_in_cell_by_text(self, text):
        cell = self.bp.add_strip_text_to_locator(*self.cell_checker, text)
        expand = (cell[0], cell[1] + "/../../../zyfra-icon")
        self.bp.click_to_element(*expand)

    def should_be_expand_cell_by_text(self, text):
        cell = self.bp.add_text_to_locator(*self.expand_cell, text)
        assert self.bp.is_element_present(*cell), 'Строки с такой ячейкой нет'

    def should_be_not_expand_cell_by_text(self, text):
        cell = self.bp.add_text_to_locator(*self.expand_cell, text)
        assert self.bp.is_not_element_present(*cell), 'Строка с такой ячейкой есть'

    def click_to_strip_text(self, text, add_locator='', index=1):
        text_cell = self.bp.add_strip_text_to_locator(*self.text_locator, text)
        complete_text = self.bp.add_index_to_locator(text_cell[0], text_cell[1] + add_locator, index)
        self.bp.click_to_element(*complete_text)

    def click_to_text(self, text, add_locator='', index=1):
        text_cell = self.bp.add_text_to_locator(*self.text_locator, text)
        complete_text = self.bp.add_index_to_locator(text_cell[0], text_cell[1] + add_locator, index)
        self.bp.click_to_element(*complete_text)


class ZQATab(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)
        self.tree_tab = (Tab.TREE_TAB[0], self.entry_locator + Tab.TREE_TAB[1])
        self.link = (Tab.LINK[0], self.entry_locator + Tab.LINK[1])

    def click_to_tree_tab_by_name(self, name):
        """
        Клик по элементу дерева с учетом пробелов
        :param name: имя вкладки в списке
        """
        tree_tab_locator = self.bp.add_strip_text_to_locator(*self.tree_tab, name)
        self.bp.click_to_element(*tree_tab_locator)

    def should_be_tree_tab_by_name_is_selected(self, name):
        tree_tab_locator = self.bp.add_strip_text_to_locator(*self.tree_tab, name)
        tree_tab_active_locator = (tree_tab_locator[0], tree_tab_locator[1] + "/../..")
        assert self.bp.get_element_attribute(*tree_tab_active_locator, 'class') \
               == 'menu-item-link active ng-star-inserted', 'Элемент дерева не выделен'

    def should_be_tree_tab_by_name(self, name):
        tree_tab_locator = self.bp.add_strip_text_to_locator(*self.tree_tab, name)
        assert self.bp.is_element_present(*tree_tab_locator), 'Такого элемента в дереве не найдено'

    def should_be_not_tree_tab_by_name(self, name):
        tree_tab_locator = self.bp.add_strip_text_to_locator(*self.tree_tab, name)
        assert self.bp.is_not_element_present(*tree_tab_locator), 'Такой элемент все еще в дереве'

    def should_be_link_by_name(self, name):
        link_locator = self.bp.add_strip_text_to_locator(*self.link, name)
        assert self.bp.is_element_present(*link_locator)

    def should_be_not_link_by_name(self, name):
        link_locator = self.bp.add_strip_text_to_locator(*self.link, name)
        assert self.bp.is_not_element_present(*link_locator)

    def click_to_link_by_name(self, name):
        link_locator = self.bp.add_strip_text_to_locator(*self.link, name)
        self.bp.click_to_element(*link_locator)


class ZQADatePicker(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)
        self.input = (Date.INPUT[0], self.entry_locator + Date.INPUT[1])
        self.calendar = (Date.CALENDAR[0], self.entry_locator + Date.CALENDAR[1])
        self.time_menu = (Date.TIME_MENU[0], self.entry_locator + Date.TIME_MENU[1])
        self.clear = (Date.CLEAR[0], self.entry_locator + Date.CLEAR[1])

    def click_to_date_input(self):
        """
        Клик по строке ввода
        """
        self.bp.click_to_element(*self.input)

    def input_text_to_date_input(self, text):
        """
        Ввести дату
        :param text: дата
        """
        self.bp.clear_input_text(*self.input, text)

    def click_to_calendar(self):
        """
        Клик по календарю
        """
        self.bp.click_to_element(*self.calendar)

    def click_to_time_button(self):
        """
        Клик по кнопке времени
        """
        self.bp.click_to_element(*self.time_menu)

    def click_to_clear_button(self):
        """
        Клик по кнопке очистки
        """
        self.bp.click_to_element(*self.clear)

    def should_be_in_date_input(self, text):
        _text = self.bp.get_element_attribute(*self.input, 'value')
        assert _text == text


class ZQAContentContainer(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)
        self.input = (Content.INPUT[0], self.entry_locator + Content.INPUT[1])
        self.save_button = (Content.SAVE_BUTTON[0], self.entry_locator + Content.SAVE_BUTTON[1])
        self.add_button = (Content.ADD_BUTTON[0], self.entry_locator + Content.ADD_BUTTON[1])

    def click_to_add_button(self):
        """
        Клик по кнопке Добавить
        """
        self.bp.click_to_element(*self.add_button)

    def click_to_save_button(self):
        """
        Клик по кнопке Сохранить
        """
        self.bp.click_to_element(*self.save_button)

    def click_to_content_text(self):
        """
        Клик по строке Содержимое
        :return:
        """
        self.bp.click_to_element(*self.input)

    def input_to_content_text(self, text):
        """
        Ввод текста содержимого
        :param text: текст содержимого
        """
        self.bp.click_to_element(*self.input)
        self.bp.clear_input_text(*self.input, text)

    def should_be_content_text(self, text):
        """
        Проверка текста внутри строки
        :param text: текст содержимого
        """
        _text = self.bp.get_element_attribute(*self.input, 'value')
        assert _text == text, 'Неверный текст содержимого'


class ZQACalendar(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)

    def click_to_mode_button(self):
        self.bp.click_to_element(*Calendar.MODE_BUTTON)

    def click_to_previous_button(self):
        self.bp.click_to_element(*Calendar.PREVIOUS_BUTTON)

    def click_to_next_button(self):
        self.bp.click_to_element(*Calendar.NEXT_BUTTON)

    def click_to_table_cell_by_text(self, text):
        cell_locator = self.bp.add_text_to_locator(*Calendar.CALENDAR_TABLE_CELL, text)
        self.bp.click_to_element(*cell_locator)

    def choose_date(self, year, month, day):
        self.bp.click_to_element(*Calendar.MODE_BUTTON)
        self.click_to_table_cell_by_text(year)
        self.bp.some_wait()
        self.click_to_table_cell_by_text(month)
        self.bp.some_wait()
        self.click_to_table_cell_by_text(day)
        self.bp.some_wait()


class ZQADropDown(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)

    def select_option_by_text(self, text):
        option_selector = self.bp.add_text_to_locator(*Drop.DROP_DOWN_OPTION, text)
        self.bp.click_to_element(*option_selector)
        self.bp.some_wait()

    def select_menu_time_line_by_text(self, text):
        menu_line = self.bp.add_text_to_locator(*Drop.MENU_LINE, text)
        self.bp.click_to_element(*menu_line)
        self.bp.some_wait()

    def select_zyfra_menu_content_by_text(self, text):
        menu_line = self.bp.add_strip_text_to_locator(*Drop.MENU_LINE, text)
        self.bp.click_to_element(*menu_line)
        self.bp.some_wait()

    def click_mat_menu_button_by_text(self, text):
        button = self.bp.add_strip_text_to_locator(*Drop.MAT_MENU_BUTTON, text)
        self.bp.click_to_element(*button)
        self.bp.some_wait(timeout=1)


class ZQAConfirmDialog(ZQAElement):
    def __init__(self, entry_locator, bp):
        super().__init__(entry_locator, bp)

    def should_be_confirm_dialog(self):
        assert self.bp.is_element_present(*Confirm.DIALOG), 'Диалог удаления не появился'

    def click_delete_button(self):
        self.bp.click_to_element(*Confirm.DIALOG_DELETE_BUTTON)
        self.bp.some_wait(timeout=1)

    def click_cancel_button(self):
        self.bp.click_to_element(*Confirm.DIALOG_CANCEL_BUTTON)

