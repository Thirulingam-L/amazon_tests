import pytest
from src.pages.Homepage import AmazonHomePage
from src.pages.Productpage import ProductPage
@pytest.fixture
def home(page):
    return AmazonHomePage(page)

@pytest.fixture
def product(page):
    return ProductPage(page)