from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Actions:
    def __init__(self, app):
        self.app = app

    def find_and_send_keys(self, xpath_locator, keys):
        wd = self.app.wd
        element = WebDriverWait(wd, 3).until(EC.element_to_be_clickable((
            By.XPATH, xpath_locator)))
        element.click()
        element.clear()
        element.send_keys(keys)

    def find_and_select_by_value(self, css_locator, value):
        wd = self.app.wd
        select_element = WebDriverWait(wd, 3).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, css_locator)))
        select = Select(select_element)
        select.select_by_value(value)
