class MyBooks:
    def __init__(self, page):
        self.page = page

    def go_to(self):
        button_catalog = self.page.locator("[data-testid='favorites']")
        button_catalog.click()

    def find_hint_text(self, text):
        locator = self.page.locator(f"text={text}")
        if locator.count() == 0:
            return None  # Texten hittades inte – hanteras i testet
        return locator

    def find_book_by_title(self, titel):
        locator = self.page.locator(f"[data-testid='fav-{titel}']")
        if locator.count() == 0:
            return None  # Texten hittades inte – hanteras i testet
        return locator