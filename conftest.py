import pytest
import selenium.webdriver
from selenium.webdriver.chrome.options import Options

from Client import Client

BASE_URL = 'http://automationpractice.com/index.php'

pytest_plugins = [
    "fixtures.pages_fixtures",
]


@pytest.fixture(autouse=True)
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("kiosk")
    browser = selenium.webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def open_home_page(driver):
    driver.get(BASE_URL)


@pytest.fixture(scope='function')
def client():
    return Client()
