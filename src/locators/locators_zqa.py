from selenium.webdriver.common.by import By


class ZQAPageLocators():
    # ZQA заголовок
    ZQA_TITLE = (By.CSS_SELECTOR, "lims-sidebar div.header")
    # Иерархия ZQA
    ZQA_SIDEBAR = (By.CSS_SELECTOR, "lims-sidebar")

    TREE_LINK_TEXT = (By.XPATH, "//div[@class='menu-item-block-name']")
    EXPAND = "/../zyfra-icon[@iconclass='arrows-chevron-right']"

    # Папка Задания
    TASKS_PACKAGE_LINK_TEXT = ()
    TASKS_PACKAGE_EXPANDED_LINK = ()
    TASKS_PACKAGE_LINK = ()
    # Ввод результатов анализов
    PATTERN_LINK_TEXT = ()
    PATTERN_LINK = ()
    # Журналы образцов
    SAMPLESLOG_LINK_TEXT = ()
    SAMPLESLOG_LINK = ()

    # Папка НСИ
    NSI_PACKAGE_LINK_TEXT = (By.XPATH, "//mat-tree-node[@role='group']//div[text()=' НСИ ']")
    NSI_PACKAGE_EXPANDED_LINK = (By.XPATH, NSI_PACKAGE_LINK_TEXT[1]+"/../zyfra-icon[@iconclass='arrows-chevron-right']")
    NSI_PACKAGE_LINK = (By.XPATH, NSI_PACKAGE_LINK_TEXT[1]+"/../../..")
    # Методики и методы
    METHODOLOGIES_LINK_TEXT = (By.XPATH, "//mat-tree-node[@role='treeitem']//div[text()=' Методики и методы ']")
    METHODOLOGIES_LINK = (By.XPATH, METHODOLOGIES_LINK_TEXT[1]+"/../../..")
    # График аналитического контроля
    GAC_LINK_TEXT = ()
    GAC_LINK = ()

    # Шаблоны образцов
    SAMPLE_TEMPLATE_LINK_TEXT = ()
    SAMPLE_TEMPLATE_LINK = ()


class ZQADialogPageLocators():
    # Оверлей
    OVERLAY = (By.XPATH, "//div[@class='cdk-overlay-container']")
    # Окно диалога
    DIALOG = (By.XPATH, "//mat-dialog-container")
    # Закрытие диалога
    CLOSE_LINK = (By.XPATH, DIALOG[1]+"//button[@zyfrabutton='mini-button']")
    # Кнопка Отмена
    CANCEL_BUTTON = (By.XPATH, DIALOG[1]+"//div[@class='dialog__actions']/button[1]")
    # Кнопка Сохранить
    SAVE_BUTTON = (By.XPATH, DIALOG[1]+"//div[@class='dialog__actions']/button[2]")
