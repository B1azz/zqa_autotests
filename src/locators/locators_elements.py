from selenium.webdriver.common.by import By


class ZQADialogLocators:
    CLOSE_BUTTON = (By.XPATH, "//div[@class='dialog__close']//button")
    DIALOG_HEADER = (By.XPATH, "//div[@class='dialog__title']")
    CANCEL_BUTTON = (By.XPATH, "//div[@class='dialog__actions']//button[@color='secondary']")
    SAVE_BUTTON = (By.XPATH, "//div[@class='dialog__actions']//button[@color='standart']")


class ZQAToolbarLocators:
    FILTER_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'sort-filter']")
    ADD_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'add-plus']")
    EDIT_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'editor-mode']")
    COPY_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'vectors-arrange-below']")
    DELETE_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'delete']")
    SEARCH_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'sort-zoom-in']")
    SEARCH_INPUT = (By.XPATH, "//input")
    REFRESH_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'arrows-cached']")
    SETTINGS_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'settings']")


class ZQATableLocators:
    BUTTON = (By.XPATH, "//button")
    CELL = (By.XPATH, "//tr//td")
    BLINE = (By.XPATH, "//tbody//tr")
    HLINE = (By.XPATH, "//thead//tr")
    FLINE = (By.XPATH, "//tfoot//tr")


class ZQADatePickerLocators:
    INPUT = (By.XPATH, "//input[1]")
    CALENDAR = (By.XPATH, "//button[1]")
    TIME_MENU = (By.XPATH, "//button[2]")
    CLEAR = (By.XPATH, "//zyfra-clear")


class ZQAContentContainerLocators:
    INPUT = (By.XPATH, "//input")
    SAVE_BUTTON = (By.XPATH, "//button[1]")
    ADD_BUTTON = (By.XPATH, "//button[2]")


class ZQAConfirmDialogLocators:
    DIALOG = (By.XPATH, "//lims-confirm-dialog")
    DIALOG_HEADER = (By.XPATH, f"{DIALOG[1]}//div[@class='title']")
    DIALOG_DELETE_BUTTON = (By.XPATH, f"{DIALOG[1]}//button[@ng-reflect-color='danger']")
    DIALOG_CANCEL_BUTTON = (By.XPATH, f"{DIALOG[1]}//button[@ng-reflect-color='secondary']")


class ZQAContextMenuLocators:
    CONTEXT_MENU = ()
    CONTEXT_MENU_LINE = ()


class ZQADropDownLocators:
    DROP_DOWN = (By.XPATH, "//zyfra-select-panel")
    DROP_DOWN_OPTION = (By.XPATH, f"{DROP_DOWN[1]}//div[@class='option']")

    MENU = (By.XPATH, "//zyfra-menu")
    MENU_LINE = (By.XPATH, f"{MENU[1]}//ul[@class='zyfra-menu-time']//li")


class ZQATabLocators:
    TAB = (By.XPATH, "//ul//li")
    TREE_TAB = (By.XPATH, "//mat-tree-node//div[@class='menu-item-block-name']")
    SPAN_TAB = (By.XPATH, "//zyfra-icon[@iconcalss='add-plus']")
    ADD_ICON = (By.XPATH, "//ul//li//span")


class ZQACalendarLocators:
    CALENDAR = (By.XPATH, "//mat-calendar")
    MODE_BUTTON = (By.XPATH, f"{CALENDAR[1]}//button[@cdkarialive='polite']")
    MODE_TEXT = (By.XPATH, f"{MODE_BUTTON[1]}//span")

    PREVIOUS_BUTTON = (By.XPATH, f"{CALENDAR[1]}//button[@class='mat-calendar-previous-button mat-icon-button']")
    NEXT_BUTTON = (By.XPATH, f"{CALENDAR[1]}//button[@class='mat-calendar-next-button mat-icon-button']")

    CALENDAR_TABLE_CELL = (By.XPATH, f"{CALENDAR[1]}//div[@class='mat-calendar-body-cell-content']")

    CALENDAR_TABLE_MONTH = (By.XPATH, f"{CALENDAR[1]}//mat-month-view//table")
    CALENDAR_TABLE_YEAR = (By.XPATH, f"{CALENDAR[1]}//mat-year-view//table")
    CALENDAR_TABLE_MULTI_YEAR = (By.XPATH, f"{CALENDAR[1]}//mat-multi-year-view//table")

