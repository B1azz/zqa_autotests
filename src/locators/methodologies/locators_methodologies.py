from selenium.webdriver.common.by import By


class MethodologiesMainLocators:
    METHODOLOGIES = (By.XPATH, "//lims-methodologies")
    COLLECTIONS_REGION = (By.XPATH, f"{METHODOLOGIES[1]}//dp-split-area[1]")

    COLLECTIONS_TOOLBAR = (By.XPATH, f"{METHODOLOGIES[1]}//lims-methodologies-sidebar/div")
    COLLECTIONS_TREE = (By.XPATH, f"{METHODOLOGIES[1]}////lims-methodologies-sidebar/lims-tree")
    METHODS_TOOLBAR = (By.XPATH, f"{METHODOLOGIES[1]}//lims-toolbar")
    METHODS_TABLE = (By.XPATH, f"{METHODOLOGIES[1]}//table")


class CollectionsDialogLocators:
    DIALOG = (By.XPATH, "//lims-dialog-create-directory")

    NAME = (By.XPATH, f"{DIALOG[1]}//div[@class='dialog__content__form__name']//input")
    CODE = (By.XPATH, f"{DIALOG[1]}//div[@class='dialog__content__form__short-name']//input")
    DESCRIPTION = (By.XPATH, f"{DIALOG[1]}//div[@class='dialog__content__form__description']//textarea")


class MethodsDialogLocators:
    DIALOG = (By.XPATH, "//lims-dialog-create-methodology")
    METHODS_TREE = (By.XPATH, f"{DIALOG[1]}//lims-tree")

    # region Общие
    NAME = (By.XPATH, f"{DIALOG[1]}//div[@class='form__name']//input")
    CODE = (By.XPATH, f"{DIALOG[1]}//div[@class='form__code']//input")
    FULL_NAME = (By.XPATH, f"{DIALOG[1]}//div[@class='form__full-name']//textarea")
    DESCRIPTION = (By.XPATH, f"{DIALOG[1]}//div[@class='form__description']//textarea")
    UNCERTAINTY = (By.XPATH, f"{DIALOG[1]}//div[@class='form__uncertainty']//label")
    # endregion

    # region Продукты
    PRODUCTS = (By.XPATH, f"{DIALOG[1]}//lims-create-methodology-products")
    PRODUCTS_DIALOG = (By.XPATH, "//qa-dialog-create-methodology-products")
    PRODUCTS_TOOLBAR = (By.XPATH, f"{PRODUCTS[1]}//div[@class='toolbar']")
    PRODUCTS_TABLE = (By.XPATH, f"{PRODUCTS[1]}//table")
    # endregion

    # region Лаборатории
    LABS = (By.XPATH, f"{DIALOG[1]}//lims-create-methodology-laboratories")
    LABS_DIALOG = (By.XPATH, "//qa-dialog-create-methodology-laboratories")
    LABS_TOOLBAR = (By.XPATH, f"{LABS[1]}//div[@class='toolbar']")
    LABS_TABLE = (By.XPATH, f"{LABS[1]}//table")
    # endregion

    # region Контексты использования
    CONTEXTS = (By.XPATH, f"{DIALOG[1]}//lims-create-methodology-contexts")
    CONTEXTS_TOOLBAR = (By.XPATH, f"{CONTEXTS[1]}//div[@class='toolbar']")
    CONTEXTS_TABLE = (By.XPATH, f"{CONTEXTS[1]}//table")
    # endregion

    # region Показатели
    TESTS = (By.XPATH, f"{DIALOG[1]}//lims-create-methodology-indicators")
    TESTS_TOOLBAR = (By.XPATH, f"{TESTS[1]}//div[@class='toolbar']")
    TESTS_TABLE = (By.XPATH, f"{TESTS[1]}//table")
    DIALOG_ANALOG = (By.XPATH, "//qa-dialog-create-methodology-indicators-analog")
    DIALOG_DISCRETE = (By.XPATH, "//qa-dialog-create-methodology-indicators-discrete")
    # endregion

    # region Расчеты
    CALCULATIONS = (By.XPATH, f"{DIALOG[1]}//lims-create-methodology-calculations")
    CALCULATIONS_DIALOG = (By.XPATH, "//qa-dialog-code-editor")
    CREATE_SCRIPT_BUTTON = (By.XPATH, f"{CALCULATIONS[1]}//button")
    # endregion

    # region Сборники
    COLLECTIONS = (By.XPATH, f"{DIALOG[1]}//lims-create-methodology-collections")
    COLLECTIONS_DIALOG = (By.XPATH, "//qa-dialog-create-methodology-collections")
    COLLECTIONS_TOOLBAR = (By.XPATH, f"{COLLECTIONS[1]}//div[@class='toolbar']")
    COLLECTIONS_TABLE = (By.XPATH, f"{COLLECTIONS[1]}//table")
    # endregion

