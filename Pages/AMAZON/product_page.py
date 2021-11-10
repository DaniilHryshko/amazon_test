from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.AddToCart)
        button.location_once_scrolled_into_view
        button.click()

