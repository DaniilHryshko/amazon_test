from Pages.AMAZON.base_page import BasePage
from time import sleep

start_page = "https://us.amazon.com/"


def test_go_to_accessories(browser):
    open_page = BasePage(browser, "https://us.amazon.com/")
    open_page.open()
    open_page.go_to_all_content()
    open_page.go_to_department()
    open_page.go_to_accessories()
    sleep(20)

