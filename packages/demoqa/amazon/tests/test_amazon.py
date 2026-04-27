def test_amazon_title(flow, page):
    flow.ensure_home()
    title = page.title()
    assert "Amazon" in title

def test_product_search(flow, product, page):
    flow.ensure_search()
    product.product_link().click()
    page.wait_for_load_state("load")

    assert product.add_to_cart_button().is_visible(), "Add to Cart button not found"
    assert product.product_title().inner_text().strip() != "", "Product title is missing"
    assert product.product_price().first.inner_text().strip() != "", "Product price is missing"

def test_pagination(flow, product, page):
    flow.ensure_product()


    page.go_back()
    product.pagination_switch(2).click()
    
    page.wait_for_load_state("load")
    assert product.page_content().is_visible(), "Page 2 List not found"