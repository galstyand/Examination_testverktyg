from behave import given, when, then
from playwright.sync_api import expect
from pages.navigation_page import PageHeader

@given(u'Användaren navigerar till Läslistan')
def step_impl(context):
    context.page.goto(context.base_url)

@when('Användaren navigerar till "{sektion}" som har testId: "{testid}"')
def step_impl(context, sektion, testid):
    if not PageHeader.find_button(context, testid).is_disabled():
        PageHeader.button_click(context, testid)

@then('blir knappen med testId: "{testid}" inaktiv')
def step_impl(context, testid):
    button = PageHeader.find_button(context, testid)
    expect(button).to_have_attribute("disabled", "")