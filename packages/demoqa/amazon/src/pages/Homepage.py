class AmazonHomePage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.amazon.com")

    def search_box(self):
        return self.page.locator("input#twotabsearchtextbox")
    
    def sort_dropdown(self):
        return self.page.locator("select#s-result-sort-select")
    
    def sort_by(self, label_text: str):
        self.sort_dropdown().select_option(label=label_text)