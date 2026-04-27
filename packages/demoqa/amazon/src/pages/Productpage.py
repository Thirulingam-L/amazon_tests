class ProductPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart_button(self):
        return self.page.locator("input#add-to-cart-button")
    
    def product_link(self):
        return self.page.locator('a[href*="samsung+galaxy+s26+ultra"]').first

    def product_title(self):
        return self.page.locator('xpath=//h1[@id="title"]//span[@id="productTitle"]')

    def product_price(self):
        return self.page.locator('xpath=//*[@id="corePrice_feature_div"]//span[@class="a-price-whole"]')
    
    def pagination_switch(self, index):
        return self.page.locator(f"a.s-pagination-item:has-text('{index}')")

    def page_content(self):
        return self.page.locator('xpath = //*[@id="search"]//span[@data-component-type="s-search-results"]')