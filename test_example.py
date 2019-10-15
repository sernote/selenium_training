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


def test_example(driver):
    driver.get('https://google.com')
    driver.find_element_by_name('q').send_keys('webdriver')
    submit_btn = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.NAME, 'btnK')))
    submit_btn.click()
    WebDriverWait(driver, 10).until(EC.title_is('webdriver - Поиск в Google'))
