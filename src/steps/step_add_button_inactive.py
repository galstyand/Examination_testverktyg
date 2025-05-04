from playwright.sync_api import expect
from pages.page_add_book import AddBook
from behave import given, when, then

@given(u'Användaren navigerar till "Lägg till bok"')
def step_go_to_add_new_book(context):
    context.page.goto(context.base_url)
    AddBook.go_to(context)

@when(u'Användaren fyller i Titel men inte Författare')
def step_fyll_title(context):
    AddBook.title_fill(context,"Title")
    AddBook.author_fill(context, "")

@then(u'"Lägg till ny bok" knappen är inaktiv')
def step_add_new_book_is_inactive(context):
    expect(AddBook.add_button(context)).to_be_disabled()

@when(u'Användaren fyller i Författare men inte Titel')
def step_fyll_author(context):
    AddBook.title_fill(context,"")
    AddBook.author_fill(context, "Author")