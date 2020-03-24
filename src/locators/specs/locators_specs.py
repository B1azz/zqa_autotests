from selenium.webdriver.common.by import By


class SpecsMainLocatorsLocators:
    SPECS = (By.XPATH, "//qa-specs")
    COLLECTIONS_REGION = (By.XPATH, f"{SPECS[1]}//dp-split-area[1]")

    COLLECTIONS_TOOLBAR = (By.XPATH, f"{SPECS[1]}//qa-specs-sidebar/div")
    COLLECTIONS_TREE = (By.XPATH, f"{SPECS[1]}//qa-specs-sidebar/lims-tree")
    SPECS_TOOLBAR = (By.XPATH, f"{SPECS[1]}//qa-specs-toolbar")
    SPECS_TABLE = (By.XPATH, f"{SPECS[1]}//table")


class CollectionsDialogPageLocators:
    DIALOG = (By.XPATH, "//qa-dialog-create-spec-digest")

    NAME = (By.XPATH, f"{DIALOG[1]}//div[@class='form__name']//input")
    CODE = (By.XPATH, f"{DIALOG[1]}//div[@class='form__code']//input")
    DESCRIPTION = (By.XPATH, f"{DIALOG[1]}//div[@class='form__description']//textarea")


class SpecsDialogLocators:
    DIALOG = (By.XPATH, "//qa-dialog-create-spec")
    SPECS_TREE = (By.XPATH, f"{DIALOG[1]}//lims-tree")

    # region Общие
    NAME = (By.XPATH, f"{DIALOG[1]}//div[@class='form__name']//input")
    CODE = (By.XPATH, f"{DIALOG[1]}//div[@class='form__code']//input")
    FULL_NAME = (By.XPATH, f"{DIALOG[1]}//div[@class='form__full-name']//textarea")
    DESCRIPTION = (By.XPATH, f"{DIALOG[1]}//div[@class='form__description']//textarea")
    DOC_SELECT = (By.XPATH, f"{DIALOG[1]}//div[@class='form__norm-docs']//zyfra-select")
    DOC_SELECT_INPUT = (By.XPATH, f"{DOC_SELECT[1]}//input")
    # endregion

    # region Продукты и лаборатории
    PRODUCTS = (By.XPATH, f"{DIALOG[1]}//qa-create-specs-products-laboratories")
    PRODUCTS_DIALOG = (By.XPATH, "//qa-dialog-specs-add-product")
    PRODUCTS_TOOLBAR = (By.XPATH, f"{PRODUCTS[1]}//div[@class='toolbar']")
    PRODUCTS_TABLE = (By.XPATH, f"{PRODUCTS[1]}//table")
    # endregion

    # region Показатели
    TESTS = (By.XPATH, f"{DIALOG[1]}//qa-create-specs-tests")
    TESTS_DIALOG = (By.XPATH, "//qa-dialog-specs-add-tests")
    TESTS_TOOLBAR = (By.XPATH, f"{TESTS[1]}//div[@class='toolbar']")
    TESTS_TABLE = (By.XPATH, f"{TESTS[1]}//table")
    # endregion

    # region Нормы продукта
    NORMS = (By.XPATH, f"{DIALOG[1]}//qa-create-specs-norms")
    NORMS_SORT_DIALOG = (By.XPATH, "//qa-dialog-specs-add-grade")
    NORMS_TESTS_DIALOG = (By.XPATH, "//qa-dialog-specs-add-test")
    NORMS_TABS = (By.XPATH, f"{NORMS[1]}//div[@class='zyfra_tab-links']")
    NORMS_TOOLBAR = (By.XPATH, f"{NORMS[1]}//div[@class='toolbar']")
    NORMS_TABLE = (By.XPATH, f"{NORMS[1]}//table")
    # endregion

    # region Сборники
    COLLECTIONS = (By.XPATH, f"{DIALOG[1]}//qa-create-specs-digest")
    COLLECTIONS_DIALOG = (By.XPATH, "//qa-dialog-specs-add-digest")
    COLLECTIONS_TOOLBAR = (By.XPATH, f"{COLLECTIONS[1]}//div[@class='toolbar']")
    COLLECTIONS_TABLE = (By.XPATH, f"{COLLECTIONS[1]}//table")
    # endregion
