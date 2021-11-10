from .base_page import BasePage
from .locators import SignInLocators
from Tools.captchaSolver import solver_captcha


class SignInPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout=10)
        self.password = ''

    def enter_login(self, login):
        Login = self.browser.find_element(*SignInLocators.LoginField)
        Login.send_keys(login)
        ContinueButton = self.browser.find_element(*SignInLocators.ContinueToPassoword_Button)
        ContinueButton.click()
        assert self.is_element_present(*SignInLocators.WrongEmail) is False, "Wrong email"
        assert self.is_element_present(*SignInLocators.ResetPassword) is False, 'Password reset required'

    def enter_password(self, password):
        self.password = password
        PassEnter = self.browser.find_element(*SignInLocators.PasswordField)
        PassEnter.send_keys(password)

    def keep_sign_in(self):
        KeepCheckPoint = self.browser.find_element(*SignInLocators.KeepSIGN_IN)
        KeepCheckPoint.click()

    def sign_in(self):
        ButtonSubmit = self.browser.find_element(*SignInLocators.SigInSubmit)
        ButtonSubmit.click()

    def check_and_submit_captcha(self):
        if self.is_element_present(*SignInLocators.captch):
            self.enter_password(self.password)

            link_captcha = self.browser.find_element(*SignInLocators.captch).get_attribute("src")
            input_captcha_field = self.browser.find_element(*SignInLocators.inputCaptchaField)
            input_captcha_field.location_once_scrolled_into_view
            input_captcha_field.send_keys(solver_captcha(link_captcha))
            self.sign_in()

    def check_warning(self):
        assert self.is_element_present(*SignInLocators.WarningLock) is False, 'Account on hold temporarily'
