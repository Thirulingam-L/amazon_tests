from playwright.sync_api import Page

class Homepage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.amazon.com")
         # Handle cookie consent banner if present
        if self.page.locator("input#sp-cc-accept").count() > 0:
            self.page.locator("input#sp-cc-accept").click()

        # Handle region/language popup if present
        if self.page.locator("button[name='glowDoneButton']").count() > 0:
            self.page.locator("button[name='glowDoneButton']").click()

        self.page.wait_for_selector("input#twotabsearchtextbox", timeout=15000)

    def search_box(self, text):
        searchbox = self.page.locator("input#twotabsearchtextbox")
        searchbox.fill(text)
        searchbox.press("Enter")
    
    def sort_dropdown(self):
        return self.page.locator("select#s-result-sort-select")
    
    def sort_by(self, label_text: str):
        self.sort_dropdown().select_option(label=label_text)