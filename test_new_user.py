import random
import string
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_regiser_new_user_and_login(app):
    app.navi.go_to_main_page()
    create_account_link = app.wd.find_element_by_xpath('//div[@id="box-account-login"]//a[contains(@href, "create_account")]')
    create_account_link.click()
    login = 'Newuser+{}@somemail.com'.format(''.join([random.choice(string.digits) for i in range(4)]))
    password = ''.join([random.choice(string.digits) for i in range(6)])
    first_name_field = app.wd.find_element_by_css_selector('input[name=firstname]')
    first_name_field.send_keys('NewUserfirst')
    lastname_field = app.wd.find_element_by_css_selector('input[name=lastname]')
    lastname_field.click()
    lastname_field.send_keys('NewUserfirst')
    address_field = app.wd.find_element_by_css_selector('input[name=address1]')
    address_field.click()
    address_field.send_keys('Somestreet')
    postcode_field = app.wd.find_element_by_css_selector('input[name=postcode]')
    postcode_field.click()
    postcode_field.send_keys('12345')
    city_field = app.wd.find_element_by_css_selector('input[name=city]')
    city_field.click()
    city_field.send_keys('New City')
    select_country_field = app.wd.find_element_by_css_selector('select[name=country_code]')
    select = Select(select_country_field)
    select.select_by_visible_text('United States')
    email_field = app.wd.find_element_by_css_selector('input[name=email]')
    email_field.click()
    email_field.send_keys(login)
    phone_field = app.wd.find_element_by_css_selector('input[name=phone]')
    phone_field.click()
    phone_field.send_keys('+79999999999')
    password_field = app.wd.find_element_by_css_selector('input[name=password]')
    password_field.click()
    password_field.send_keys(password)
    confirmed_password_field = app.wd.find_element_by_css_selector('input[name=confirmed_password]')
    confirmed_password_field.click()
    confirmed_password_field.send_keys(password)
    app.wd.find_element_by_css_selector('button[type=submit][name=create_account]').click()
    app.wd.find_element_by_xpath('//a[contains(@href, "logout")]').click()
    login_field_main_page = WebDriverWait(app.wd, 3).until(EC.element_to_be_clickable((By.NAME, 'email')))
    login_field_main_page.click()
    login_field_main_page.send_keys(login)
    password_field = app.wd.find_element_by_css_selector('input[name=password]')
    password_field.click()
    password_field.send_keys(password)
    app.wd.find_element_by_css_selector('button[type=submit][name=login]').click()
