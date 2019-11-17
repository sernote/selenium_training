import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import os
import time


def test_item_open(app):
    re_template = '\((.*)\)'
    app.navi.go_to_main_page()
    item_element_on_main_page = app.wd.find_elements_by_xpath('//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"]')[0]
    item_name_on_main_page = item_element_on_main_page.find_element_by_css_selector('div.name').text
    item_regular_price_on_main_page = item_element_on_main_page.find_element_by_css_selector('.regular-price')
    item_regular_price_on_main_page_text = item_regular_price_on_main_page.text
    reg_price_color_m = item_regular_price_on_main_page.value_of_css_property('color')
    item_regular_price_on_main_page_color =re.search(re_template, reg_price_color_m).group(1).split(', ')[:3]
    item_regular_price_on_main_page_text_decoration = item_regular_price_on_main_page.value_of_css_property('text-decoration')
    item_regular_price_on_main_page_size = item_regular_price_on_main_page.value_of_css_property('font-size')[:-2]
    # проверяем что цвет обычной цены серый
    assert all(x == item_regular_price_on_main_page_color[0] for x in item_regular_price_on_main_page_color)
    # проверяем что обычная цена перечеркнута
    assert 'line-through' in item_regular_price_on_main_page_text_decoration
    item_campaign_price_on_main_page = item_element_on_main_page.find_element_by_css_selector('.campaign-price')
    item_campaign_price_on_main_page_text = item_campaign_price_on_main_page.text
    camp_price_color_m = item_campaign_price_on_main_page.value_of_css_property('color')
    item_campaign_price_on_main_page_color = re.search(re_template, camp_price_color_m).group(1).split(', ')[:3]
    item_campaign_price_on_main_page_text_decoration = item_campaign_price_on_main_page.value_of_css_property('font-weight')
    item_campaign_price_on_main_page_size = item_campaign_price_on_main_page.value_of_css_property('font-size')[:-2]
    # проверяем что цвет новой цены - красный
    assert item_campaign_price_on_main_page_color[1] == '0' and item_campaign_price_on_main_page_color[2] == '0'
    # проверяем что новая цена выделена
    assert int(item_campaign_price_on_main_page_text_decoration) >= 700
    # проверяем что размер обычной цены меньше чем новой
    assert float(item_regular_price_on_main_page_size) < float(item_campaign_price_on_main_page_size)
    # переходим на страницу товара
    item_element_on_main_page.click()
    item_element_on_item_page = app.wd.find_element_by_css_selector('div#box-product')
    item_name_on_item_page = item_element_on_item_page.find_element_by_css_selector('h1').text
    item_regular_price_on_item_page = item_element_on_item_page.find_element_by_css_selector('.regular-price')
    item_regular_price_on_item_page_text = item_regular_price_on_item_page.text
    reg_price_color_i = item_regular_price_on_item_page.value_of_css_property('color')
    item_regular_price_on_item_page_color = re.search(re_template, reg_price_color_i).group(1).split(', ')[:3]
    item_regular_price_on_item_page_text_decoration = item_regular_price_on_item_page.value_of_css_property('text-decoration')
    item_regular_price_on_item_page_size = item_regular_price_on_item_page.value_of_css_property('font-size')[:-2]
    # проверяем что цвет обычной цены серый
    assert all(x == item_regular_price_on_item_page_color[0] for x in item_regular_price_on_item_page_color)
    # проверяем что обычная цена перечеркнута
    assert 'line-through' in item_regular_price_on_item_page_text_decoration
    item_campaign_price_on_item_page = item_element_on_item_page.find_element_by_css_selector('.campaign-price')
    item_campaign_price_on_item_page_text = item_campaign_price_on_item_page.text
    camp_price_color_i = item_campaign_price_on_item_page.value_of_css_property('color')
    item_campaign_price_on_item_page_color = re.search(re_template, camp_price_color_i).group(1).split(', ')[:3]
    item_campaign_price_on_item_page_text_decoration = item_campaign_price_on_item_page.value_of_css_property('font-weight')
    item_campaign_price_on_item_page_size = item_campaign_price_on_item_page.value_of_css_property('font-size')[:-2]
    # проверяем что цвет новой цены - красный
    assert item_campaign_price_on_item_page_color[1] == '0' and item_campaign_price_on_item_page_color[2] == '0'
    # проверяем что новая цена выделена
    assert int(item_campaign_price_on_item_page_text_decoration) >= 700
    # проверяем что размер обычной цены меньше чем новой
    assert float(item_regular_price_on_item_page_size) < float(item_campaign_price_on_item_page_size)
    # проверяем что название товара одинановые
    assert item_name_on_main_page == item_name_on_item_page
    # проверяем что обычные цены на товар одинаковы
    assert item_regular_price_on_main_page_text == item_regular_price_on_item_page_text
    # проверяем что новые цены на товар одинаковы
    assert item_campaign_price_on_main_page_text == item_campaign_price_on_item_page_text


def test_add_item(app):
    item_salt = ''.join([random.choice(string.digits) for i in range(6)])
    app.login_as_admin()
    app.navi.go_to_catalog_page()
    add_item_btn = WebDriverWait(app.wd, 3).until(EC.element_to_be_clickable((
        By.XPATH, '//a[@class="button" and contains(@href, "edit_product")]')))
    add_item_btn.click()
    time.sleep(2)
    new_item_name = 'New product{}'.format(item_salt)
    app.do.find_and_send_keys('//input[@name="name[en]"]', new_item_name)
    app.do.find_and_send_keys('//input[@name="code"]', item_salt)
    general_page_category_box = app.wd.find_element_by_xpath('//input[@type = "checkbox" and @name ="categories[]"'
                                                         'and @data-name="Rubber Ducks"]')
    if general_page_category_box.get_attribute('checked') is not True:
        general_page_category_box.click()
    select_category_field = app.wd.find_element_by_css_selector('select[name=default_category_id]')
    select = Select(select_category_field)
    select.select_by_visible_text('Rubber Ducks')
    general_page_gender_box = app.wd.find_element_by_xpath('//td[contains(text(),"Unisex")]/..//input[@type="checkbox"]')
    general_page_gender_box.click()
    app.do.find_and_send_keys('//input[@name="quantity"]', '2,00')
    select_quantity_unit_id = app.wd.find_element_by_css_selector('select[name=quantity_unit_id]')
    select = Select(select_quantity_unit_id)
    select.select_by_visible_text('pcs')
    app.do.find_and_select_by_value("select[name=delivery_status_id]", '1')
    select_sold_out_status_id = app.wd.find_element_by_css_selector('select[name=sold_out_status_id]')
    select = Select(select_sold_out_status_id)
    select.select_by_visible_text('Temporary sold out')
    path_to_item_image = os.path.dirname(os.path.abspath(__file__))+'/test_pic.png'
    app.wd.find_element_by_xpath('//input[@type="file" and @name="new_images[]"]').send_keys(path_to_item_image)
    app.do.find_and_send_keys("//input[@name='date_valid_from']", '17112019')
    app.do.find_and_send_keys("//input[@name='date_valid_to']", '17112020')
    # переходим на таб "информация"
    app.wd.find_element_by_xpath("//a[@href='#tab-information']").click()
    time.sleep(2)
    app.do.find_and_select_by_value("select[name=manufacturer_id]", '1')
    app.do.find_and_send_keys("//input[@name='keywords']", 'Item {} test keywords'.format(item_salt))
    app.do.find_and_send_keys("//input[@name='short_description[en]']", 'Test item {}'.format(item_salt))
    app.do.find_and_send_keys("//div[@class='trumbowyg-editor']", 'Test item {} full description'.format(item_salt))
    app.do.find_and_send_keys("//input[@name='head_title[en]']", 'Test item {}'.format(item_salt))
    app.do.find_and_send_keys("//input[@name='meta_description[en]']", 'Test item {}'.format(item_salt))
    # переходим на таб "информация"
    app.wd.find_element_by_xpath("//a[@href='#tab-prices']").click()
    time.sleep(2)
    app.do.find_and_send_keys("//input[@name='purchase_price']", '123')
    app.do.find_and_select_by_value("select[name=purchase_price_currency_code]", 'USD')
    app.do.find_and_send_keys("//input[@name='prices[USD]']", '123')
    app.do.find_and_send_keys("//input[@name='prices[EUR]']", '123')
    # сохраняем
    app.wd.find_element_by_xpath('//button[@name="save"]').click()
    time.sleep(2)
    assert app.wd.find_element_by_xpath('//td/a[contains(text(), "{}")]'.format(new_item_name))
