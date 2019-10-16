import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.find_element_by_name('username').click()
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').click()
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
