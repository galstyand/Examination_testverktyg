from playwright.sync_api import expect
from pages.page_add_book import AddBook
from pages.page_catalog import Catalog
from behave import given, when, then

@given(u'användaren navigerar till \'Lägg till bok\'')
def step_given_navigate_to_add_book(context):
    context.page.goto(context.base_url)
    AddBook.go_to(context)

@when(u'användaren fyller i \'Titel\'')
def step_fill_title(context):
    AddBook.title_fill(context, "Book title")

@when(u'användaren fyller i \'Författare\'')
def step_fill_author(context):
    AddBook.author_fill(context, "Book author")

@when(u'användaren klickar på \'Lägg till ny bok\' knappen')
def step_click_add(context):
    AddBook.add_click(context)

@then(u'boken läggs till som en ny rad i \'Katalog\'')
def step_impl(context):
    Catalog.go_to(context)
    book = Catalog.find_book_by_title(context, "Book title")
    expect(book).to_be_visible()