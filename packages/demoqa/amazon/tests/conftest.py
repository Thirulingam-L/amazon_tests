from src.fixtures.amazon_fixtures import *
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="session")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()