from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True

    def go_to_all_content(self):
        self.browser.find_element(*BasePageLocators.AllContentButton).click()

    def go_to_department(self):
        self.browser.find_element(*BasePageLocators.ElectronicDepartment).click()

    def go_to_accessories(self):
        self.browser.find_element(*BasePageLocators.Accessories).click()

    def go_to_sign_in(self):
        link = self.browser.find_element(*BasePageLocators.SignIn).get_attribute("href")
        self.browser.get(link)

    def go_to_cart(self):
        self.browser.find_element(*BasePageLocators.CartLink).click()

