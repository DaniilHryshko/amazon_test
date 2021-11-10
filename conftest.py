import pytest
import undetected_chromedriver.v2  as uc
from time import sleep


@pytest.fixture(scope="function")
def browser(request):
    browser = uc.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()