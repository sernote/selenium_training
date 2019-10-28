
def test_left_menu(app):
    wd = app.wd
    app.login_as_admin()
    left_panel = wd.find_element_by_id('box-apps-menu')
    left_panel_tabs = left_panel.find_elements_by_id('app-')
    for i in left_panel_tabs:
        num = left_panel_tabs.index(i)
        wd.find_elements_by_xpath('*//ul[@id = "box-apps-menu"]/li')[num].click()
        assert wd.find_element_by_tag_name('h1').is_displayed()


