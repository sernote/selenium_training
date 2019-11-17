
class Navigation:
    def __init__(self, app):
        self.app = app

    def go_to_contries_page(self):
        wd = self.app.wd
        wd.get('http://localhost/litecart/admin/?app=countries&doc=countries')

    def go_to_geo_zones(self):
        wd = self.app.wd
        wd.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')

    def go_to_catalog_page(self):
        wd = self.app.wd
        wd.get('http://localhost/litecart/admin/?app=catalog&doc=catalog')

    def go_to_main_page(self):
        wd = self.app.wd
        wd.get('http://localhost/litecart/en/')
