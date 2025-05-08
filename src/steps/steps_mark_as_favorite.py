from behave import when, then
from pages.page_catalog import Catalog
from pages.page_my_books import MyBooks
from playwright.sync_api import expect

@when('Användaren klickar på stjärnan på boken med titel "{boktitel}"')
def step_klick_on_heart(context, boktitel):
    Catalog.click_on_heart(context, boktitel)


@then(u'boken med titel "{boktitel}" är i listan')
def step_check_book_is_in_favorites(context, boktitel):
    expect(MyBooks.find_book_by_title(context, boktitel)).to_contain_text(boktitel)