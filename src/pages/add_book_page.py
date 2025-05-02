class AddBook:
    def __init__(self, page):
        self.page = page

    def go_to(self):
        button_add_book = self.page.locator("[data-testid='add-book']")
        button_add_book.click()

    def title(self, title_text):
        textbox_title = self.page.locator("[data-testid='add-input-title']")
        textbox_title.fill(title_text)

    def author(self, author_text):
        textbox_author = self.page.locator("[data-testid='add-input-author']")
        textbox_author.fill(author_text)

    def add(self):
        button_add = self.page.locator("[data-testid='add-submit']")
        button_add.click()