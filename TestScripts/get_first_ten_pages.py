from Pages.AMAZON.pagination_products_page import PaginationProductsPage


def get_names(browser):
    open_page = PaginationProductsPage(browser, browser.current_url)
    open_page.open()
    open_page.get_name_products()


def get_and_go_to_first_link(browser):
    open_page = PaginationProductsPage(browser, browser.current_url)
    open_page.open()
    open_page.get_and_go_first_link()

