from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_add_and_delete_item_in_basket(app):
    wd = app.wd

    # логично вынести метод добавления в соотвествующий класс помощник, но оставил тут для проверки ДЗ :)
    def add_items_to_basket(num):
        for i in range(1, num+1):
            app.navi.go_to_main_page()
            app.do.find_and_click('//li[@class="product column shadow hover-light"]')
            counter_locator = '//div[@id="cart-wrapper"]//span[@class="quantity"]'
            WebDriverWait(wd, 3).until(EC.presence_of_element_located((
                By.XPATH, counter_locator)))
            if len(app.wd.find_elements_by_xpath('//select[@name="options[Size]"]')) > 0:
                app.do.find_and_select_by_value('select', 'Small')
            app.do.find_and_click('//button[@name="add_cart_product"]')
            WebDriverWait(wd, 3).until(EC.text_to_be_present_in_element((By.XPATH, counter_locator), str(i)))

    def remove_items_in_basket(num):
        for i in range(1, num+1):
            summary = WebDriverWait(wd, 3).until(EC.presence_of_element_located((By.XPATH, '//div[@id="checkout-summary-wrapper"]//tbody/tr[2]')))
            WebDriverWait(wd, 3).until(
                EC.presence_of_element_located((By.XPATH, '//button[@name="remove_cart_item"]'))).click()
            if len(app.wd.find_elements_by_xpath('//em[contains(text(), "There are no items in your cart")]')) > 0:
                break
            WebDriverWait(wd, 3).until(EC.staleness_of(summary))
            WebDriverWait(wd, 3).until(EC.presence_of_element_located((By.XPATH, '//div[@id="checkout-summary-wrapper"]//tbody/tr[2]')))

    add_items_to_basket(3)
    app.do.find_and_click('//div[@id="cart"]')
    remove_items_in_basket(3)
