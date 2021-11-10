from Pages.AMAZON.product_page import ProductPage


def add_product(browser):
    page = ProductPage(browser, browser.current_url)
    page.open()
    page.add_to_cart()
