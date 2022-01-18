import pytest

from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.my_account_page import MyAccountPage


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(autouse=True)
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(autouse=True)
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture(autouse=True)
def my_account_page(driver):
    return MyAccountPage(driver)
