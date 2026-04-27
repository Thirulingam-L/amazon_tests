from src.pages.Productpage import Productpage
from src.pages.Homepage import Homepage
from playwright.sync_api import Page

class AmazonFlow:

    def __init__(self, page: Page, home: Homepage, product: Productpage):
        self.page = page
        self.home = home
        self.product = product

    def ensure_home(self):
        if "amazon" not in self.page.url:
            self.home.goto()

    def ensure_search(self, text = "samsung galaxy s26 ultra"):
        self.ensure_home()
        if text.split()[0] not in self.page.url:
            self.home.search_box(text)
            self.page.wait_for_load_state("load")
            self.home.sort_by("Price: High to Low")
            self.page.wait_for_load_state("load")

    def ensure_product(self):
        self.ensure_search()
        if "/dp/" not in self.page.url:
            self.product.product_link().click()
            self.page.wait_for_load_state("load")