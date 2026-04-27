import os
import pytest
from playwright.sync_api import sync_playwright

pytest_plugins = ["src.fixtures.amazon_fixtures"]

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    args=["--disable-blink-features=AutomationControlled"]
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only act after test execution (not setup/teardown)
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            os.makedirs("screenshots", exist_ok=True)
            file_name = f"screenshots/{item.name}.png"
            page.screenshot(path=file_name)