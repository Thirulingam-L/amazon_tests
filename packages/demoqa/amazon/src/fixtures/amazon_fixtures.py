import pytest
from src.pages.Homepage import Homepage
from src.pages.Productpage import Productpage
from src.flows.amazon_flow import AmazonFlow
@pytest.fixture
def home(page):
    return Homepage(page)

@pytest.fixture
def product(page):
    return Productpage(page)

@pytest.fixture
def flow(page, home, product):
    return AmazonFlow(page, home, product)
