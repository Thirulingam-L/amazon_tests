import pytest
from playwright.sync_api import sync_playwright

pytest_plugins = ["src.fixtures.amazon_fixtures"]

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(
        
    )
    yield context
    context.close()


@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()
