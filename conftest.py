import logging
import sys
import pytest
import socket
import requests

from pytest_reportportal import RPLogger, RPLogHandler
from selenium import webdriver

from src.pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="remote", help="Choose browser")
    parser.addoption('--browser_image', action='store', default="chrome", help="Choose browser")
    parser.addoption('--vrs', action='store', default="79.0", help="Choose version")


@pytest.fixture(scope="function")
def browser1(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "remote":
        print("\nstart chrome browser for test...")
        browser_image = request.config.getoption("browser_image")
        vrs = request.config.getoption("vrs")

        browser = webdriver.Remote(
            command_executor="http://192.168.101.57:4444/wd/hub",
            desired_capabilities={
                "browserName": browser_image,
                "version": vrs,
                "enableVNC": True,
                "enableVideo": False,
                "name": socket.gethostname(),
                "labels": {"environment": "UDP"}
            })
    elif browser_name == "chrome":
        print("\nstart chrome browser for test...")
        browser = webdriver.Chrome()
    elif browser_name == "edge":
        print("\nstart edge browser for test...")
        browser = webdriver.Remote(
            command_executor="http://192.168.101.36:4444/",
            desired_capabilities={
                "browserName": "MicrosoftEdge",
                "version": "",
                "platform": "WINDOWS",
                "ms:inPrivate": True
            })
    else:
        raise pytest.UsageError("--browser_name should be remote or chrome")

    yield browser
    print("\nquit browser..")
    browser.quit()


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
