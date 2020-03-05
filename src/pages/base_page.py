import inspect
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, text_to_be_present_in_element, \
    staleness_of, presence_of_element_located, visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        """
        Конструктор браузера
        :param browser: передача браузера
        :param url: передача адреса
        :param timeout: неявное ожидание в секундах
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Открыть страницу в развернутом окне
        """
        self.browser.maximize_window()
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Проверка существует ли элемент
        :param how: метод поиска элемента
        :param what: путь до элемента
        :return: Если элемент найден, то True
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def some_wait(timeout=0.33):
        """
        Обычная задержка
        :param timeout: секунды ожидания
        """
        time.sleep(timeout)

    def is_not_element_present(self, how, what, timeout=5):
        """
        Проверка, что элемент не появился в течении отведенного времени
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param timeout: секунды ожидания
        :return: Если элемент найден, то True
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def get_element_text(self, how, what):
        """
        Вернуть текст внутри локатора
        :param how: метод поиска элемента
        :param what: путь до элемента
        :return: Текст внутри локатора
        """
        element = self.browser.find_element(how, what)
        text = element.text
        return text

    def input_text(self, how, what, text):
        """
        Добавить текст в элемент-инпут
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param text: вводимый текст
        """
        element = self.browser.find_element(how, what)
        element.send_keys(text)

    def clear_input_text(self, how, what, text):
        """
        Очистить инпут и добавить в него текст
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param text: вводимый текст
        """
        element = self.browser.find_element(how, what)
        element.clear()
        element.send_keys(text)

    def clear_text(self, how, what):
        """
        Очистить инпут
        :param how: метод поиска элемента
        :param what: путь до элемента
        """
        element = self.browser.find_element(how, what)
        element.clear()

    def click_to_element(self, how, what):
        """
        Одинарный клик по элементу
        :param how: метод поиска элемента
        :param what: путь до элемента
        """
        button = self.browser.find_element(how, what)
        button.click()

    def hover_to_element(self, how, what):
        """
        Навестись на элемент
        :param how: метод поиска элемента
        :param what: путь до элемента
        """
        element = self.browser.find_element(how, what)
        element.hover()

    def check_element(self, how, what):
        """
        Пометить чекер
        :param how: метод поиска элемента
        :param what: путь до элемента
        """
        element = self.browser.find_element(how, what)
        element.check()

    def get_element_attribute(self, how, what, attribute):
        """
        Получить значение указанного атрибута элемента
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param attribute: наименование атрибута
        :return: значение указанного атрибута
        """
        element = self.browser.find_element(how, what)
        return element.get_attribute(attribute)
        # print(f"\n{attribute} = {value}")

    def is_selected(self, how, what):
        element = self.browser.find_element(how, what)
        result = element.is_selected()
        print(f"\nis selected = {result}")
        return result

    def get_count(self, how, what):
        """
        Сосчитать количество элементов с определенным локатором
        :param how: метод поиска элемента
        :param what: путь до элемента
        :return: количество элементов
        """
        elements = self.browser.find_elements(how, what)
        elements_count = len(elements)
        return elements_count

    def get_elements_text(self, how, what):
        """
        Получить текст со всех найденных эелементов
        :param how: метод поиска элемента
        :param what: путь до элемента
        :return: Список всех полученных текстов
        """
        texts = []
        elements = self.browser.find_elements(how, what)
        for element in elements:
            texts.append(element.text)
        return texts

    def wait_until_is_clickable(self, how, what, timeout=5):
        """
        Дождаться, пока элемент не станет кликабельным
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param timeout: секунды ожидания
        """
        selector = (how, what)
        WebDriverWait(self.browser, timeout).until(
            element_to_be_clickable(selector)
        )
        self.some_wait()

    def wait_until_is_text_in_element(self, how, what, text, timeout=5):
        """
        Дождаться, пока в элементе не появится нужный текст
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param text: искомый текст
        :param timeout: секунды ожидания
        """
        selector = (how, what)
        WebDriverWait(self.browser, timeout).until(
            text_to_be_present_in_element(selector, text)
        )
        self.some_wait()

    def wait_until_is_staleness_of(self, how, what, timeout=5):
        """
        Дождаться, пока элемент не пропадет
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param timeout: секунды ожидания
        """
        selector = (how, what)
        WebDriverWait(self.browser, timeout).until(
            staleness_of(selector)
        )
        self.some_wait()

    def wait_until_is_element_presence(self, how, what, timeout=5):
        """
        Дождаться, пока элемент не появится в DOM-дереве
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param timeout: секунды ожидания
        """
        selector = (how, what)
        WebDriverWait(self.browser, timeout).until(
            presence_of_element_located(selector)
        )
        self.some_wait()

    def wait_until_is_element_located(self, how, what, timeout=5):
        """
        Дождаться, пока элемент не появится в DOM-дереве и не станет виден
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param timeout: секунды ожидания
        """
        selector = (how, what)
        WebDriverWait(self.browser, timeout).until(
            visibility_of_element_located(selector)
        )
        self.some_wait()

    @staticmethod
    def add_text_to_locator(how, what, text):
        """
        Добавить в локатор [text()=''] с пробелами в начала и конце текста
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param text: параметр текст для локатора
        :return: локатор с добавленным текстом
        """
        some_text = f"[text()=' {text} ']"
        new_locator = (how, what + some_text)
        return new_locator

    @staticmethod
    def add_strip_text_to_locator(how, what, text):
        """
        Добавить в локатор [text()=''] без пробелов в начала и конце текста
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param text: параметр текст для локатора
        :return: локатор с добавленным текстом
        """
        some_text = f"[text()='{text}']"
        new_locator = (how, what + some_text)
        return new_locator

    @staticmethod
    def add_index_to_locator(how, what, number):
        """
        Добавить в локатор [index] без пробелов в начала и конце текста
        :param how: метод поиска элемента
        :param what: путь до элемента
        :param number: параметр индекс для локатора
        :return: локатор с добавленным идексом
        """
        numbered_what = f"({what})[{number}]"
        new_locator = (how, numbered_what)
        return new_locator

    def collect_text_from_elements(self, how, what):
        texts = []
        elements = self.browser.find_elements(how, what)
        for element in elements:
            texts.append(element.text)
        return texts

    @staticmethod
    def get_button_by_icon_class(icon_class):
        """
        Получить локатор кнопки, используя словарь
        :param icon_class: класс кнопки
        :return: локатор кнопки в xpath
        """
        return f"//zyfra-icon[@iconclass='{icon_class}']"

    def get_path_locators(self, cls):
        """
        Возвращает коллекцию локаторов из класса в виде пары : метод проверки и путь локатора
        :param cls: класс с локаторами
        """
        locators = []
        for item in inspect.getmembers(cls, lambda a: not (inspect.isroutine(a))):
            if item[0] is '__class__':
                break
            locators.append(item[1])

        return locators

    def go_to_tab_by_name(self, locator, name):
        """
        Перейти на вкладку по имени
        :param locator: имя локатора
        :param name: имя вкладки
        """
        tab = self.add_text_to_locator(*locator, name)
        self.click_to_element(*tab)