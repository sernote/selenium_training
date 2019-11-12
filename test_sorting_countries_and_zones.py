"""Сделайте сценарии, которые проверяют сортировку стран и геозон (штатов) в учебном приложении litecart.

2) на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
зайти в каждую из стран и проверить, что зоны расположены в алфавитном порядке"""


def test_countries_sorting(app):
    app.login_as_admin()
    app.navi.go_to_contries_page()
    rows = app.wd.find_elements_by_css_selector('.row')
    countries_names = [x.find_element_by_tag_name('a').get_attribute('text') for x in rows]
    assert countries_names == sorted(countries_names), 'Страны отсортированы не по алфавиту'
    countries_with_many_zones = []
    for row in rows:
        if int(row.find_elements_by_tag_name('td')[5].text) != 0:
            countries_with_many_zones.append(row)
    if len(countries_with_many_zones) > 0:
        countries_to_zonez_check = {x.find_element_by_tag_name('a').get_attribute('text')
                                    :x.find_element_by_tag_name('a').get_attribute('href')
                                    for x in countries_with_many_zones}
        for name, link in countries_to_zonez_check.items():
            app.wd.get(link)
            table_zones = app.wd.find_element_by_css_selector('table#table-zones')
            zones = table_zones.find_elements_by_css_selector('tr:not(.header)')[:-1]
            zones_names = [x.find_elements_by_tag_name('td')[2].text for x in zones]
            assert zones_names == sorted(zones_names), 'Сортировка зон на странице страны {} не в алфавитном порядке'.format(name)


def test_geo_zones_sorting(app):
    app.login_as_admin()
    app.navi.go_to_geo_zones()
    country_links = app.wd.find_elements_by_css_selector('table.dataTable .row a:not([title=Edit])')
    countries = {x.get_attribute('text'): x.get_attribute('href') for x in country_links}
    for name, link in countries.items():
        app.wd.get(link)
        zones = app.wd.find_elements_by_xpath('//table[@id="table-zones"]//tr[not(@class="header")]/td[3]//option[@selected]')
        zones_names = [x.text for x in zones]
        assert zones_names == sorted(zones_names), 'Сортировка зон на странице страны {} не в алфавитном порядке'.format(name)
