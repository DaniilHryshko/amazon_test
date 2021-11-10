from Pages.AMAZON.product_page import ProductPage


def test_add_product(browser, product_link):
    cart_page = ProductPage(browser, product_link)
    cart_page.open()
    cart_page.add_to_cart()
