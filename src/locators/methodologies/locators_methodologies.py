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
# endregion
# region Продукты
# endregion
# region Лаборатории
# endregion
# region Контексты использования
# endregion
# region Показатели
# endregion
# region Расчеты
# endregion
# region Сборники
# endregion

