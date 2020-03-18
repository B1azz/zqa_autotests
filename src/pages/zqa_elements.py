from src.locators.locators_elements import ZQAToolbarLocators as Tlbr, \
    ZQATableLocators as Tbl, \
    ZQATabLocators as Tab, \
    ZQADatePickerLocators as Date, \
    ZQAContentContainerLocators as Content, \
    ZQACalendarLocators as Calendar, \
    ZQADropDownLocators as Drop


class ZQAElement:
    def __init__(self, entry_locator, base_page):
        self.entry_locator = entry_locator
        self.base_page = base_page


class ZQAToolbar(ZQAElement):
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)
        self.filter_button_locator = (Tlbr.FILTER_BUTTON[0], self.entry_locator + Tlbr.FILTER_BUTTON[1])
        self.add_button_locator = (Tlbr.ADD_BUTTON[0], self.entry_locator + Tlbr.ADD_BUTTON[1])
        self.edit_button_locator = (Tlbr.EDIT_BUTTON[0], self.entry_locator + Tlbr.EDIT_BUTTON[1])
        self.copy_button_locator = (Tlbr.COPY_BUTTON[0], self.entry_locator + Tlbr.COPY_BUTTON[1])
        self.delete_button_locator = (Tlbr.DELETE_BUTTON[0], self.entry_locator + Tlbr.DELETE_BUTTON[1])
        self.search_button_locator = (Tlbr.SEARCH_BUTTON[0], self.entry_locator + Tlbr.SEARCH_BUTTON[1])
        self.refresh_button_locator = (Tlbr.REFRESH_BUTTON[0], self.entry_locator + Tlbr.REFRESH_BUTTON[1])
        self.settings_button_locator = (Tlbr.SETTINGS_BUTTON[0], self.entry_locator + Tlbr.SETTINGS_BUTTON[1])
        self.search_input_locator = (Tlbr.SEARCH_INPUT[0], self.entry_locator + Tlbr.SEARCH_INPUT[1])

    def click_soft_filter_button(self):
        """
        Клик по по кнопке Фильтр
        """
        self.base_page.click_to_element(*self.filter_button_locator)

    def click_add_button(self):
        """
        Клик по кнопке Создать
        """
        self.base_page.click_to_element(*self.add_button_locator)

    def click_edit_button(self):
        """
        Клик по кнопке Редактировать
        """
        self.base_page.click_to_element(*self.edit_button_locator)

    def click_copy_button(self):
        """
        Клик по кнопке Копировать
        """
        self.base_page.click_to_element(*self.copy_button_locator)

    def click_delete_button(self):
        """
        Клик по кнопке Удалить
        """
        self.base_page.click_to_element(*self.delete_button_locator)

    def click_search_button(self):
        """
        Клик по кнопке Поиск
        """
        self.base_page.click_to_element(*self.search_button_locator)

    def click_refresh_button(self):
        """
        Клик по кнопке Обновить
        """
        self.base_page.click_to_element(*self.refresh_button_locator)

    def click_settings_button(self):
        """
        Клик по кнопке Настройки
        """
        self.base_page.click_to_element(*self.settings_button_locator)

    def click_search_input(self):
        """
        Клик по полю ввода для поиска
        """
        self.base_page.click_to_element(*self.search_input_locator)

    def input_search_text(self, text):
        """
        Ввод текста
        :param text: текст
        """
        self.base_page.input_text(*self.search_input_locator, text)

    def clear_search_text(self):
        """ Очистить текст """
        self.base_page.clear_text(*self.search_input_locator)


class ZQATable(ZQAElement):
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)
        self.column_locator = (Tbl.BUTTON[0], self.entry_locator + Tbl.BUTTON[1])
        self.cell_locator = (Tbl.CELL[0], self.entry_locator + Tbl.CELL[1])
        self.table_line_locator = (Tbl.BLINE[0], self.entry_locator + Tbl.BLINE[1])

    def click_to_table_column_by_name(self, name):
        """
        Клик по наименованию столбца таблицы
        :param name: наименование столбца
        """
        column = self.base_page.add_text_to_locator(*self.column_locator, name)
        self.base_page.click_to_element(*column)

    def click_to_table_line_by_cell_text(self, text):
        """
        Клик по ячейке таблицы с тектом
        :param text: текст в ячейке
        """
        cell_by_text = self.base_page.add_text_to_locator(*self.cell_locator, text)
        self.base_page.click_to_element(*cell_by_text)

    def click_to_table_line_by_number(self, number):
        """
        Клик по строке по порядковому номеру в таблице
        :param number: номер строки
        """
        table_line = self.base_page.add_index_to_locator(*self.table_line_locator, number)
        self.base_page.click_to_element(*table_line)

    def choose_table_line_by_cell_text(self, text):
        """
        Выбор строки по тексту ячейки внутри, с проверкой
        :param text: текст в ячейке
        """
        cell_by_text = self.base_page.add_text_to_locator(*self.cell_locator, text)
        table_line = (cell_by_text[0], cell_by_text[1] + "/..")
        if "active" not in self.base_page.get_element_attribute(*table_line, "class"):
            self.base_page.click_to_element(*cell_by_text)

    def choose_table_line_by_number(self, number):
        """
        Выбор строки по порядковому номеру в таблице, с проверкой
        :param number: номер строки
        """
        table_line = self.base_page.add_index_to_locator(*self.table_line_locator, number)
        if "active" not in self.base_page.get_element_attribute(*table_line, "class"):
            self.base_page.click_to_element(*table_line)


class ZQATab(ZQAElement):
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)
        self.tree_tab = (Tab.TREE_TAB[0], self.entry_locator + Tab.TREE_TAB[1])

    def click_to_tree_tab_by_name(self, name):
        """
        Клик по элементу дерева с учетом пробелов
        :param name: имя вкладки в списке
        """
        new_locator = self.base_page.add_text_to_locator(*self.tree_tab, name)
        self.base_page.click_to_element(*new_locator)


class ZQADatePicker(ZQAElement):
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)
        self.input = (Date.INPUT[0], self.entry_locator + Date.INPUT[1])
        self.calendar = (Date.CALENDAR[0], self.entry_locator + Date.CALENDAR[1])
        self.time_menu = (Date.TIME_MENU[0], self.entry_locator + Date.TIME_MENU[1])
        self.clear = (Date.CLEAR[0], self.entry_locator + Date.CLEAR[1])

    def click_to_date_input(self):
        """
        Клик по строке ввода
        """
        self.base_page.click_to_element(*self.input)

    def input_text_to_date_input(self, text):
        """
        Ввести дату
        :param text: дата
        """
        self.base_page.clear_input_text(*self.input, text)

    def click_to_calendar(self):
        """
        Клик по календарю
        """
        self.base_page.click_to_element(*self.calendar)

    def click_to_time_button(self):
        """
        Клик по кнопке времени
        """
        self.base_page.click_to_element(*self.time_menu)

    def click_to_clear_button(self):
        """
        Клик по кнопке очистки
        """
        self.base_page.click_to_element(*self.clear)


class ZQAContentContainer(ZQAElement):
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)
        self.input = (Content.INPUT[0], self.entry_locator + Content.INPUT[1])
        self.save_button = (Content.SAVE_BUTTON[0], self.entry_locator + Content.SAVE_BUTTON[1])
        self.add_button = (Content.ADD_BUTTON[0], self.entry_locator + Content.ADD_BUTTON[1])

    def click_to_add_button(self):
        """
        Клик по кнопке Добавить
        """
        self.base_page.click_to_element(*self.add_button)

    def click_to_save_button(self):
        """
        Клик по кнопке Сохранить
        """
        self.base_page.click_to_element(*self.save_button)

    def click_to_content_text(self):
        """
        Клик по строке Содержимое
        :return:
        """
        self.base_page.click_to_element(*self.input)

    def input_to_content_text(self, text):
        """
        Ввод текста содержимого
        :param text: текст содержимого
        """
        self.base_page.clear_input_text(*self.input, text)


class ZQACalendar(ZQAElement):
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)

    def click_to_mode_button(self):
        self.base_page.click_to_element(*Calendar.MODE_BUTTON)

    def click_to_previous_button(self):
        self.base_page.click_to_element(*Calendar.PREVIOUS_BUTTON)

    def click_to_next_button(self):
        self.base_page.click_to_element(*Calendar.NEXT_BUTTON)

    def click_to_table_cell_by_text(self, text):
        cell_locator = self.base_page.add_text_to_locator(*Calendar.CALENDAR_TABLE_CELL, text)
        self.base_page.click_to_element(*cell_locator)


class ZQADropDown(ZQAElement):
    def __init__(self, entry_locator, base_page):     
        super().__init__(entry_locator, base_page)

    def select_option_by_text(self, text):
        option_selector = self.base_page.add_text_to_locator(*Drop.DROP_DOWN_OPTION, text)
        self.base_page.click_to_element(*option_selector)
        
    def select_menu_line_by_text(self, text):
        menu_line = self.base_page.add_text_to_locator(*Drop.MENU_LINE, text)
        self.base_page.click_to_element(menu_line)
