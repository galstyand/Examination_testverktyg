from behave import given, when, then
from pages.page_my_books import MyBooks
from pages.page_catalog import Catalog
from playwright.sync_api import expect

@given(u'Användaren står i Katalog')
def step_navigate_to_katalog(context):
    context.page.goto(context.base_url)


@when(u'Det finns inga böcker favoritmarkerade')
def step_check_starred_books_count(context):
    selected = Catalog.get_books_with_selected_star(context)
    assert len(selected) == 0, f"Det finns {len(selected)} böcker markerade som favorit"

@when(u'användaren navigerar till Mina Böcker')
def step_navigate_to_my_books(context):
    MyBooks.go_to(context)


@then('ska "{expected_text}" texten visas')
def step_check_the_text_is_displayed(context, expected_text):
    expect(MyBooks.find_hint_text(context, expected_text)).to_contain_text(expected_text)

@when(u'användaren markerar en bok som favorit')
def step_mark_a_book_as_favorite(context):
    Catalog.click_on_heart(context, "Hur man tappar bort sin TV-fjärr 10 gånger om dagen")


@then(u'ska "{expected_text}" texten inte visas')
def step_check_the_text_is_not_displayed(context, expected_text):
    if MyBooks.find_hint_text(context, expected_text) is None:
        pass