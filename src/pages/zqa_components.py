from selenium.webdriver.common.by import By


class ZQAComponent:
    """ Главный компонент """
    def __init__(self, entry_locator, base_page):
        self.entry_locator = entry_locator
        self.base_page = base_page


class ZQAToolbar(ZQAComponent):
    """
    Панель инструментов
    """
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)

        self.filter_button = "//zyfra-icon[@iconclass = 'sort-filter']"
        self.add_button = "//zyfra-icon[@iconclass = 'add-plus']"
        self.edit_button = "//zyfra-icon[@iconclass = 'editor-mode']"
        self.copy_button = "//zyfra-icon[@iconclass = 'vectors-arrange-below']"
        self.delete_button = "//zyfra-icon[@iconclass = 'delete']"
        self.search_button = "//zyfra-icon[@iconclass = 'sort-zoom-in']"
        self.search_input = "//input"
        self.refresh_button = "//zyfra-icon[@iconclass = 'arrows-cached']"
        self.settings_button = "//zyfra-icon[@iconclass = 'settings']"

    def click_soft_filter_button(self):
        """
        Клик по по кнопке Фильтр
        """
        filter_button_locator = (By.XPATH, self.entry_locator + self.filter_button)
        self.base_page.click_to_element(*filter_button_locator)

    def click_create_button(self):
        """
        Клик по кнопке Создать
        """
        create_button_locator = (By.XPATH, self.entry_locator + self.add_button)
        self.base_page.click_to_element(*create_button_locator)

    def click_edit_button(self):
        """
        Клик по кнопке Редактировать
        """
        edit_button_locator = (By.XPATH, self.entry_locator + self.edit_button)
        self.base_page.click_to_element(*edit_button_locator)

    def click_copy_button(self):
        """
        Клик по кнопке Копировать
        """
        copy_button_locator = (By.XPATH, self.entry_locator + self.copy_button)
        self.base_page.click_to_element(*copy_button_locator)

    def click_delete_button(self):
        """
        Клик по кнопке Удалить
        """
        delete_button_locator = (By.XPATH, self.entry_locator + self.delete_button)
        self.base_page.click_to_element(*delete_button_locator)

    def click_search_button(self):
        """
        Клик по кнопке Поиск
        """
        search_button_locator = (By.XPATH, self.entry_locator + self.search_button)
        self.base_page.click_to_element(*search_button_locator)

    def click_refresh_button(self):
        """
        Клик по кнопке Обновить
        """
        refresh_button_locator = (By.XPATH, self.entry_locator + self.refresh_button)
        self.base_page.click_to_element(*refresh_button_locator)

    def click_settings_button(self):
        """
        Клик по кнопке Настроики
        """
        settings_button_locator = (By.XPATH, self.entry_locator + self.settings_button)
        self.base_page.click_to_element(*settings_button_locator)

    def click_search_input(self):
        """
        Клик по полю ввода для поиска
        """
        search_input_locator = (By.XPATH, self.entry_locator + self.search_input)
        self.base_page.click_to_element(*search_input_locator)

    def input_search_text(self, text):
        """
        Ввод текста
        :param text: текст
        """
        search_text_locator = (By.XPATH, self.entry_locator + self.search_input)
        self.base_page.input_text(*search_text_locator, text)

    def clear_text(self):
        """ Очистить текст """
        new_locator = (By.XPATH, self.entry_locator + self.search_input)
        self.base_page.clear_text(*new_locator)


class ZQATable(ZQAComponent):
    """ Таблица """
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)

        self.button = "//button"
        self.cell = "//tr//td"
        self.bline = "//tbody//tr"
        self.hline = "//thead//tr"
        self.fline = "//tfoot//tr"

    def click_to_table_column_by_name(self, name):
        """
        Клик по наименованию столбца таблицы
        :param name: наименование столбца
        """
        new_locator = (By.XPATH, self.entry_locator + self.button)
        column = self.base_page.add_text_to_locator(* new_locator, name)
        self.base_page.click_to_element(*column)

    def click_to_table_line_by_cell_text(self, text):
        """
        Клик по ячейке таблицы с тектом
        :param text: текст в ячейке
        """
        new_locator = (By.XPATH, self.entry_locator + self.cell)
        cell_by_text = self.base_page.add_text_to_locator(*new_locator, text)
        self.base_page.click_to_element(*cell_by_text)

    def click_to_table_line_by_number(self, number):
        """
        Клик по строке по порядковому номеру в таблице
        :param number: номер строки
        """
        new_locator = (By.XPATH, self.entry_locator + self.bline)
        table_line = self.base_page.add_index_to_locator(*new_locator, number)
        self.base_page.click_to_element(*table_line)

    def choose_table_line_by_cell_text(self, text):
        """
        Выбор строки по тексту ячейки внутри, с проверкой
        :param text: текст в ячейке
        """
        new_locator = (By.XPATH, self.entry_locator + self.cell)
        cell_by_text = self.base_page.add_text_to_locator(*new_locator, text)
        table_line = (cell_by_text[0], cell_by_text[1] + "/..")
        if "active" not in self.base_page.get_attribute(*table_line, "class"):
            self.base_page.click_to_element(*cell_by_text)

    def choose_table_line_by_number(self, number):
        """
        Выбор строки по порядковому номеру в таблице, с проверкой
        :param number: номер строки
        """
        new_locator = (By.XPATH, self.entry_locator + self.bline)
        table_line = self.base_page.add_index_to_locator(*new_locator, number)
        if "active" not in self.base_page.get_attribute(*table_line, "class"):
            self.base_page.click_to_element(*table_line)


class ZQAButtons(ZQAComponent):
    """ Обычные кнопки """
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)

        self.close = "//zyfra-icon[@iconclass='cancel-close']"
        self.button = "//button//span[@class='zyfra_button-content']"

    def click_to_button_close(self):
        """ Клик по кнопке Закрыть """
        new_locator = (By.XPATH, self.entry_locator + self.close)
        self.base_page.click_to_element(*new_locator)

    def click_to_button_save(self):
        """ Клик по кнопке Сохранить """
        new_locator = (By.XPATH, self.entry_locator + self.button + f"[text()='Сохранить']")
        self.base_page.click_to_element(*new_locator)

# вместо "Отмена" необходимо подставить текст в соответсвии с локализацией, для подстановки используем словарь
    def click_to_button_cancel(self):
        """ Клик по кнопке Отмена """
        new_locator = (By.XPATH, self.entry_locator + self.button + f"[text()='Отмена']")
        self.base_page.click_to_element(*new_locator)

    def click_to_button_ok(self):
        """ Клик по кнопке Ок """
        new_locator = (By.XPATH, self.entry_locator + self.button + f"[text()='Ок']")
        self.base_page.click_to_element(*new_locator)

    def click_to_button_select(self):
        """ Клик по кнопке Выбрать """
        new_locator = (By.XPATH, self.entry_locator + self.button + f"[text()='Выбрать']")
        self.base_page.click_to_element(*new_locator)

    def click_to_button_delete(self):
        """ Клик по кнопке Удалить """
        new_locator = (By.XPATH, self.entry_locator + self.button + f"[text()='Удалить']")
        self.base_page.click_to_element(*new_locator)

    def click_to_button_canceling(self):
        """ Клик по кнопке Отменить """
        new_locator = (By.XPATH, self.entry_locator + self.button + f"[text()=' Отменить ']")
        self.base_page.click_to_element(*new_locator)

    def click_to_button_apply(self):
        """ Клик по кнопке Применить """
        new_locator = (By.XPATH, self.entry_locator + self.button + f"[text()=' Применить ']")
        self.base_page.click_to_element(*new_locator)


class ZQAListDropDown(ZQAComponent):
    """ Выпадающий список """
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)

        self.drop_down_line = "//zyfra-option//div//div[@class='option']"

    def click_to_line_list_by_name(self, name):
        """
        Клик по строке в списке по имени
        :param name: имя строки в списке
        """
        line_locator = (By.XPATH, self.entry_locator + self.drop_down_line)
        new_locator = self.base_page.add_text_to_locator(*line_locator, name)
        self.base_page.click_to_element(*new_locator)


class ZQAListMenuTab(ZQAComponent):
    """ Список меню """
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)

        self.tab = "//ul//li"
        self.tree_tab = "//mat-tree-node//div[@class='menu-item-block-name']"
        self.add_icon = "//zyfra-icon[@iconcalss='add-plus']"
        self.span_tab = "//ul//li//span"

    def click_to_tree_tab_by_name(self, name):
        """
        Клик по элементу дерева с учетом пробелов
        :param name: имя вкладки в списке
        """
        tree_tab = (By.XPATH, self.entry_locator + self.tree_tab)
        new_locator = self.base_page.add_text_to_locator(*tree_tab, name)
        self.base_page.click_to_element(*new_locator)

    def click_to_tab_by_name(self, name):
        """
        Клик по вкладке с учетом пробелов
        :param name: имя вкладки в списке
         """
        tab_locator = (By.XPATH, self.entry_locator + self.tab)
        new_locator = self.base_page.add_text_to_locator(*tab_locator, name)
        self.base_page.click_to_element(*new_locator)

    def click_to_icon_add(self):
        """ Клик по иконке добавить """
        new_locator = (By.XPATH, self.entry_locator + self.add_icon)
        self.base_page.click_to_element(*new_locator)

    def click_to_tab_strip_by_name(self, name):
        """
        Клик по вкладке c учетом отсутсвующих пробелов
        :param name: имя вкладки в списке
        """
        # вместо "Продукты" необходимо подставить текст в соответсвии с локализацией, для подстановки используем словарь
        tab_locator = (By.XPATH, self.entry_locator + self.span_tab)
        new_locator = self.base_page.add_strip_text_to_locator(*tab_locator, name)
        self.base_page.click_to_element(*new_locator)


class ZQAListContextMenu(ZQAComponent):
    def __init__(self, entry_locator, base_page):
        super().__init__(entry_locator, base_page)

        self.context_option = ""

    def click_to_context_line(self, name):
        context_line = self.context_option + f"[text()=' {name} ']"
        new_locator = (By.XPATH, self.entry_locator + context_line)
        self.base_page.click_to_element(*new_locator)

