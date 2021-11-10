from Pages.AMAZON.sign_in_page import SignInPage


def sign_in(browser, login, password, page):
    opened_page = SignInPage(browser, page)
    opened_page.open()
    opened_page.go_to_sign_in()
    opened_page.enter_login(login)
    opened_page.enter_password(password)
    opened_page.keep_sign_in()
    opened_page.sign_in()
    opened_page.check_and_submit_captcha()
    opened_page.check_warning()


