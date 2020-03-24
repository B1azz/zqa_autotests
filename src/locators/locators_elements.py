from selenium.webdriver.common.by import By


class ZQADialogLocators:
    CLOSE_BUTTON = (By.XPATH, "//div[@class='dialog__close']//button")
    DIALOG_HEADER = (By.XPATH, "//div[@class='dialog__title']")
    CANCEL_BUTTON = (By.XPATH, "//div[@class='dialog__actions']//button[@color='secondary']")
    SAVE_BUTTON = (By.XPATH, "//div[@class='dialog__actions']//button[@color='standart']")
    CHECKER = (By.XPATH, "//div[@class='dialog__actions__checkbox-is-active']//label")


class ZQAToolbarLocators:
    FILTER_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'sort-filter']")
    ADD_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'add-plus']")
    EDIT_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'editor-mode']")
    COPY_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'vectors-arrange-below']")
    DIAPASON_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'arrows-arrow-expand-horizontal']")
    DELETE_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'delete']")
    SEARCH_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'sort-zoom-in']")
    SEARCH_INPUT = (By.XPATH, "//input")
    REFRESH_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'arrows-cached-1']")
    SETTINGS_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass = 'settings']")


class ZQAAddDialogLocators:
    HEADER = (By.XPATH, "//div[@class ='dialog__toolbar__title']/div")
    TOOLBAR = (By.XPATH, "//div[@class ='dialog__content__search']")
    TABLE = (By.XPATH, "//table")
    CLOSE_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass='cancel-close']")
    SELECT_BUTTON = (By.XPATH, "//div[@class='dialog__actions']//button[@color='success']")


class ZQATestDialogLocators:
    CLOSE_BUTTON = (By.XPATH, "//zyfra-icon[@iconclass='cancel-close']")
    CANCEL_BUTTON = (By.XPATH, "//div[@class='dialog__actions']//button[@color='secondary']")
    SAVE_BUTTON = (By.XPATH, "//div[@class='dialog__actions']//button[@color='success']")
    HEADER = (By.XPATH, "//div[@class ='dialog__toolbar__title']/div")
    DIALOG_INPUTS = (By.XPATH, "//div[@class='dialog__content__form__body']")
    NAME_SELECT = (By.XPATH, f"{DIALOG_INPUTS[1]}//zyfra-select")
    NAME_INPUT = (By.XPATH, f"{NAME_SELECT[1]}//input")
    CODE = (By.XPATH, f"{DIALOG_INPUTS[1]}//zyfra-input[1]//input")
    OFFICIAL_NAME = (By.XPATH, f"{DIALOG_INPUTS[1]}//zyfra-input[2]//input")
    DESCRIPTION = (By.XPATH, f"{DIALOG_INPUTS[1]}//zyfra-input//textarea")

    TABS = (By.XPATH, "//div[@class='dialog__content__form__tabs']")
    COMMON_TAB = (By.XPATH, f"{TABS[1]}//div[@class='dialog__content__form__tabs__tab'][1]//button")
    ANALYTICS_TAB = (By.XPATH, f"{TABS[1]}//div[@class='dialog__content__form__tabs__tab'][2]//button")

    UNIT_CLASSES = (By.XPATH, "//div[@class='dialog__content__form__common__unit-classes']//zyfra-select")
    UNIT_CLASSES_INPUT = (By.XPATH, f"{UNIT_CLASSES[1]}//input")
    UNITS = (By.XPATH, "//div[@class='dialog__content__form__common__units']//zyfra-select")
    UNITS_INPUT = (By.XPATH, f"{UNITS[1]}//input")
    UNIT_DIGITS = (By.XPATH, "//div[@class='dialog__content__form__common__unit-digits']//input")
    DIGITAL_SETS = (By.XPATH, "//div[@class='dialog__content__form__common__unit-classes']//zyfra-select")
    DIGITAL_SETS_INPUT = (By.XPATH, f"{DIGITAL_SETS[1]}//input")

    ANALYTICS_TABLE = (By.XPATH, "//div[@class='dialog__content__form__types ng-star-inserted']//table")


class ZQACodeEditorLocators:
    HEADER = (By.XPATH, "//div[@class ='dialog__toolbar__title']/div")
    AREA = ()
    CANCEL_BUTTON = (By.XPATH, "//div[@class='dialog__actions']//button[@color='secondary']")
    SAVE_BUTTON = (By.XPATH, "//div[@class='dialog__actions']//button[@color='success']")


class ZQATableLocators:
    BUTTON = (By.XPATH, "//button")
    CELL = (By.XPATH, "//tr//td/span")
    DIALOG_CELL = (By.XPATH, "//tr//td")
    INPUT = (By.XPATH, "//")
    BLINE = (By.XPATH, "//tbody//tr")
    HLINE = (By.XPATH, "//thead//tr")
    FLINE = (By.XPATH, "//tfoot//tr")

    CELL_BUTTON = (By.XPATH, f"{BLINE[1]}//td//zyfra-icon")
    CELL_EXPAND = (By.XPATH, f"{BLINE[1]}//")
    CELL_CHECKER = (By.XPATH, f"{BLINE[1]}//label//span")


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
    DROP_DOWN = (By.XPATH, "//zyfra-overlay-container")
    DROP_DOWN_OPTION = (By.XPATH, f"{DROP_DOWN[1]}//div[@class='option']")

    MENU = (By.XPATH, "//zyfra-menu")
    MENU_LINE = (By.XPATH, f"{MENU[1]}//ul[@class='zyfra-menu-time']//li")

    MAT_MENU = (By.XPATH, "//div[@class='mat-menu-content']")
    MAT_MENU_BUTTON = (By.XPATH, f"{MAT_MENU[1]}//button")


class ZQATabLocators:
    TAB = (By.XPATH, "//ul//li")
    TREE_TAB = (By.XPATH, "//mat-tree-node//div[@class='menu-item-block-name']")
    SPAN_TAB = (By.XPATH, "//zyfra-icon[@iconcalss='add-plus']")
    ADD_ICON = (By.XPATH, "//ul//li//span")
    LINK = (By.XPATH, "//a")


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


