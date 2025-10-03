import pytest
import conftest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smok
class TestLogin:
    def test_login(self):
        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_sucesso()


