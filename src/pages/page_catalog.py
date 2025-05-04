class Catalog:
    def __init__(self, page):
        self.page = page

    def go_to(self):
        button_catalog = self.page.locator("[data-testid='catalog']")
        button_catalog.click()

    def find_book_by_title(self, title):
        book_with_title = self.page.locator(f"[data-testid='star-{title}']")
        return book_with_title

    def click_on_heart(self, title):
        button_heart = self.page.locator(f"[data-testid='star-{title}']")
        button_heart.click()