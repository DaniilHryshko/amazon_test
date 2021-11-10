from selenium.webdriver.common.by import By


class BasePageLocators:
    CartLink = (By.CSS_SELECTOR, 'span[id="nav-cart-count"]')
    OrderList = (By.CSS_SELECTOR, 'a[id="nav-orders"]')
    SignIn = (By.CSS_SELECTOR, 'a[id="nav-link-accountList"]')

    # Go to department
    AllContentButton = (By.CSS_SELECTOR, 'i.hm-icon.nav-sprite')
    ElectronicDepartment = (By.CSS_SELECTOR, 'a.hmenu-item[data-menu-id="5"]')
    Accessories = (By.XPATH, '//a[contains(text(), "Accessories & Supplies")]')


class SignInLocators:
    LoginField = (By.CSS_SELECTOR, 'input[id="ap_email"]')
    ContinueToPassoword_Button = (By.CSS_SELECTOR, 'input[id="continue"][class="a-button-input"]')
    PasswordField = (By.CSS_SELECTOR, 'input[id="ap_password"]')
    KeepSIGN_IN = (By.CSS_SELECTOR, 'input[name=rememberMe]')
    SigInSubmit = (By.CSS_SELECTOR, 'input[id="signInSubmit"]')
    captch = (By.CSS_SELECTOR, 'img[alt="Visual CAPTCHA image, continue down for an audio option."]')
    inputCaptchaField = (By.CSS_SELECTOR, 'input[id="auth-captcha-guess"]')
    WarningLock = (By.CSS_SELECTOR, 'div.a-box.a-alert.a-alert-warning')
    Locators = (By.CSS_SELECTOR, 'span[class="a-size-medium.transaction-approval-word-break.a-text-bold"]')
    WrongEmail = (By.XPATH, '//h4[contains(text(), "There was a problem")]')
    ResetPassword = (By.XPATH, '//h2[contains(text(), "Password reset required")]')


class ProductPageLocators:
    AddToCart = (By.CSS_SELECTOR, 'input[id="add-to-cart-button"]')


class PaginationProductsPageLocators:
    NamesOfProducts = (By.CSS_SELECTOR, 'span.a-size-base.a-color-base.a-text-normal')
    # крч, не понимаю что тут не так. Запустил тест с этим локатором в коммандной строке, сайт отдаёт значения 50/50 не меняя локатора
    NamesOfProductsV2 = (By.CSS_SELECTOR, 'a.a-link-normal.a-text-normal')
    NextPage = (By.CSS_SELECTOR, 'li.a-last')
    FirstProdcutLink = (By.CSS_SELECTOR, 'img[data-image-latency="s-product-image"]')

