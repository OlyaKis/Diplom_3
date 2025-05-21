import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import os


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("browser")
    if browser == "chrome":
        chromedriver_path = "/usr/local/bin/chromedriver"
        if not os.path.exists(chromedriver_path):
            raise RuntimeError(f"chromedriver not found at {chromedriver_path}")
        service = ChromeService(executable_path=chromedriver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1280,1024")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1280")
        options.add_argument("--height=1024")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser '{browser}' is not supported")
    yield driver
    driver.quit()
