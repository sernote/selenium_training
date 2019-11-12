import re


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

