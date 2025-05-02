class PageHeader:
    def __init__(self, page):
        self.page = page

    def button_click(self, testId):
        button = self.page.locator(f"[data-testid='{testId}']")
        button.click()

    def find_button(self, testId):
        button = self.page.locator(f"[data-testid='{testId}']")
        return button