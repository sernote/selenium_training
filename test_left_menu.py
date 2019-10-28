
def test_left_menu(app):
    wd = app.wd
    app.login_as_admin()
    left_panel_tabs = wd.find_elements_by_css_selector('#box-apps-menu #app-')
    for i in left_panel_tabs:
        num = left_panel_tabs.index(i)
        tab_locator = '*//ul[@id = "box-apps-menu"]/li'
        wd.find_elements_by_xpath(tab_locator)[num].click()
        assert wd.find_element_by_tag_name('h1').is_displayed()
        inserted_tabs = wd.find_elements_by_xpath(tab_locator)[num].find_elements_by_css_selector('.docs li')
        if len(inserted_tabs) > 0:
            for n in inserted_tabs:
                index = inserted_tabs.index(n)
                wd.find_elements_by_xpath(tab_locator)[num].find_elements_by_css_selector(
                    '.docs li')[index].click()
                assert wd.find_element_by_tag_name('h1').is_displayed()




