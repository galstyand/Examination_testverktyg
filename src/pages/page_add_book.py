class AddBook:
    def __init__(self, page):
        self.page = page

    def go_to(self):
        button_add_book = self.page.locator("[data-testid='add-book']")
        button_add_book.click()

    def title_fill(self, title_text):
        textbox_title = self.page.locator("[data-testid='add-input-title']")
        textbox_title.fill(title_text)

    def author_fill(self, author_text):
        textbox_author = self.page.locator("[data-testid='add-input-author']")
        textbox_author.fill(author_text)

    def add_click(self):
        button_add = self.page.locator("[data-testid='add-submit']")
        button_add.click()

    def add_button(self):
        button_add = self.page.locator("[data-testid='add-submit']")
        return button_add