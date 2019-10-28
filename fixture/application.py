from selenium import webdriver


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()

    def login_as_admin(self):
        self.wd.get('http://localhost/litecart/admin/')
        self.wd.find_element_by_name('username').click()
        self.wd.find_element_by_name('username').send_keys('admin')
        self.wd.find_element_by_name('password').click()
        self.wd.find_element_by_name('password').send_keys('admin')
        self.wd.find_element_by_name('login').click()

    def destroy(self):
        self.wd.quit()
