
def test_all_products_have_one_sticker(app):
    app.go_to_main_page()
    products = app.wd.find_elements_by_xpath('*//li[@class = "product column shadow hover-light"]')
    for product in products:
        assert len(product.find_elements_by_xpath('.//div[contains(@class, "sticker")]')) == 1

