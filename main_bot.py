# python3 -m pytest -v main_bot.py -ra


from TestScripts import sign_in
import pytest

start_page = "https://us.amazon.com/"
valid_accounts = []


def get_accounts():
    accounts = open("./Data/not_checked_accounts.txt", 'r')
    list_of_account = [line.strip() for line in accounts]
    accounts.close()
    return list_of_account


def write_valid_accounts(accounts):
    new_valid_accounts = open("./Data/valid_accounts.txt", 'a')
    for acc in accounts:
        new_valid_accounts.write(acc + '\n')
    new_valid_accounts.close()


class TestCheckAccounts:

    def there_are_products_on_first_ten_pages(self):
        pass

    @pytest.mark.parametrize('login', get_accounts())
    def test_account_session_registration(self, browser, login):
        password = "qwe123"
        sign_in(browser, login, password, start_page)
        valid_accounts.append(login)

    def test_finally(self):
        write_valid_accounts(valid_accounts)
