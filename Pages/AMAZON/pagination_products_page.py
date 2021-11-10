from .base_page import BasePage
from .locators import PaginationProductsPageLocators


class PaginationProductsPage(BasePage):

    def get_name_products(self):
        items = self.browser.find_elements(*PaginationProductsPageLocators.NamesOfProductsV2)
        texts = [item.text for item in items]
        print(len(texts))
        assert len(texts) > 34, "amount of links are too small"
        self.browser.find_element(*PaginationProductsPageLocators.NextPage).click()

    def get_and_go_first_link(self):
        self.browser.find_element(*PaginationProductsPageLocators.FirstProdcutLink).click()
