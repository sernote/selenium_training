from selenium import webdriver
from fixture.navigation import Navigation
from fixture.actions import Actions


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.navi = Navigation(self)
        self.do = Actions(self)
        self.wd.implicitly_wait(2)

    def login_as_admin(self):
        self.wd.get('http://localhost/litecart/admin/')
        self.wd.find_element_by_name('username').click()
        self.wd.find_element_by_name('username').send_keys('admin')
        self.wd.find_element_by_name('password').click()
        self.wd.find_element_by_name('password').send_keys('admin')
        self.wd.find_element_by_name('login').click()

    def go_to_main_page(self):
        self.wd.get('http://localhost/litecart')

    def destroy(self):
        self.wd.quit()
