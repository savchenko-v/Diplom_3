import pytest
import requests
from selenium import webdriver
from data import Urls
from helpers import TestDataHelper
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.get(Urls.BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def create_and_delete_user():  # создание данных для юзера для тестов и последующее удаление
    user_data = TestDataHelper.create_user_data()
    create_response = requests.post(Urls.CREATE_USER_API, json=user_data)

    yield user_data

    token = create_response.json()['accessToken']
    TestDataHelper.delete_user(token)


@pytest.fixture
def login(driver, create_and_delete_user):
    base_page = BasePage(driver)
    user = create_and_delete_user
    base_page.wait_and_click_element(PersonalAccountLocators.PERSONAL_ACCOUNT)
    base_page.login_user(user['email'], user['password'])

    return driver
