def test_amazon_title(home, page):
    home.goto()
     # Handle cookie consent banner if present
    if page.locator("input#sp-cc-accept").is_visible():
        page.locator("input#sp-cc-accept").click()

    # Handle region/language popup if present
    if page.locator("button[name='glowDoneButton']").is_visible():
        page.locator("button[name='glowDoneButton']").click()

    page.wait_for_selector("input#twotabsearchtextbox", timeout=15000)
    title = page.title()
    assert "Amazon" in title

def test_product_search(home, product, page):
    home.search_box().fill("samsung galaxy s26 ultra")
    home.search_box().press("Enter")

    page.wait_for_load_state("load")
    home.sort_by("Price: High to Low")

    page.wait_for_load_state("load")
    product.product_link().click()

    page.wait_for_load_state("load")
    assert product.add_to_cart_button().is_visible(), "Add to Cart button not found"
    assert product.product_title().inner_text().strip() != "", "Product title is missing"
    assert product.product_price().first.inner_text().strip() != "", "Product price is missing"

def test_pagination(product, page):
    page.go_back()
    product.pagination_switch(2).click()
    
    page.wait_for_load_state("load")
    assert product.page_content().is_visible(), "Page 2 List not found"