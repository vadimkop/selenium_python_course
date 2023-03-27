import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    return webdriver.Chrome()


@pytest.fixture(scope="function")
def set_up(driver):
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    driver.maximize_window()
    yield
    driver.quit()