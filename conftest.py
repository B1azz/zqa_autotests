import logging
import sys
import pytest
import requests

from pytest_reportportal import RPLogger, RPLogHandler
from selenium import webdriver

from src.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()

    browser = webdriver.Chrome()
    yield browser
    print("\n\nQuit browser.")
    browser.quit()


@pytest.fixture(scope="session")
def rp_logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if hasattr(request.node.config, 'py_test_service'):
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)

    rp_handler.setLevel(logging.INFO)
    return logger


@pytest.fixture()
def login_to_polygon(browser):
    link = "http://192.168.101.126/"
    username = "admin"
    password = "admin"
    login = LoginPage(browser, link)
    login.open()
    login.login_user(username, password)
