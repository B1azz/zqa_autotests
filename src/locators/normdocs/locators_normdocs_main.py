from selenium.webdriver.common.by import By


class NormDocsMain:
    NORM_DOCS = (By.XPATH, "//qa-normdocs")

    TYPEDOCS_TOOLBAR = (By.XPATH, f"{NORM_DOCS[1]}//qa-normdocs-sidebar/div")
    TYPEDOCS_TREE = (By.XPATH, f"{NORM_DOCS[1]}//qa-normdocs-sidebar/lims-tree")
    DOCS_TOOLBAR = (By.XPATH, f"{NORM_DOCS[1]}//lims-toolbar")
    DOCS_TABLE = (By.XPATH, f"{NORM_DOCS[1]}//table")


class NormDocsDialog:
    DIALOG = (By.XPATH, "//qa-dialog-create-normdoc")
    DIALOG_TREE = (By.XPATH, f"({DIALOG[1]}//lims-tree")

# region Общие
    NAME = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width50'])[1]//input")
    CODE = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width50'])[2]//input")
    TYPEDOC = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width50'])[3]//zyfra-select")
    ORDER_NUMBER = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width50'])[4]//input")
    DESCRIPTION = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width100'])//textarea")
    ACCEPT_DATE = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width33'])[1]//zyfra-datepicker")
    START_DATE = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width33'])[2]//zyfra-datepicker")
    STOP_DATE = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width33'])[3]//zyfra-datepicker")
# endregion

# region Содержимое
    CONTENT_TABLE = (By.XPATH, f"{DIALOG[1]}//div[@class='entity-container']")
    CONTENT_TABLE_REMOVE = (By.XPATH, f"{CONTENT_TABLE[1]}//zyfra-icon[@iconclass='cancel-close']")
    CONTENT_TABLE_ADD = (By.XPATH, f"{CONTENT_TABLE[1]}//zyfra-icon[@iconclass='add-plus']")
    CONTENT_TABLE_ITEM = (By.XPATH, f"{CONTENT_TABLE[1]}//div[@class='entity__title']")

    CONTENT_NAME = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width100'])[1]//input")

    CONTENT_CONTAINER = (By.XPATH, f"({DIALOG[1]}//div[@class='field-width100'])[2]")
# endregion

# region Положения нормативного документа
    STATE_TOOLBAR = (By.XPATH, f"({DIALOG[1]}//div[@class='toolbar']")

    STATE_TABLE = (By.XPATH, f"({DIALOG[1]}//table")
# endregion
