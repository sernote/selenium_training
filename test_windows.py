from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_link_opening_in_new_windows(app):
    wd = app.wd
    app.login_as_admin()
    app.navi.go_to_contries_page()
    app.do.find_and_click('//a[@class="button"]')
    links = wd.find_elements_by_xpath('//form[@method="post"]//a[@target="_blank"]')
    main_window = wd.current_window_handle
    main_title = wd.title
    for link in links:
        all_windows = wd.window_handles
        link.click()
        WebDriverWait(wd, 3).until(EC.new_window_is_opened(all_windows))
        new_window = [x for x in wd.window_handles if x not in all_windows][0]
        wd.switch_to.window(new_window)
        assert main_title != wd.title
        wd.close()
        wd.switch_to.window(main_window)



