import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

@pytest.fixture
def chromium_page_old() -> Page: # type: ignore
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page: # type: ignore
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()

'''
@pytest.fixture
def chromium_page_with_data() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        context.storage_state(path='browser-state.json')

        # Checking header of Dashboard page presence and text
        dashboard_page_title = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_page_title).to_be_visible()
        expect(dashboard_page_title).to_have_text("Dashboard")
        chromium_page.wait_for_timeout(5000)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
'''