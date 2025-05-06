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

    def get_books_with_selected_star(self):
        books = self.page.locator("div.book")
        count = books.count()
        selected_books = []

        for i in range(count):
            book = books.nth(i)
            star = book.locator(".star.selected")
            if star.count() > 0:
                selected_books.append(book)

        return selected_books
