import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestAddProduto():
    def test_add_produto(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"

        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.adicionar_item_carrinho(produto_1)
        home_page.acessa_carrinho()

        carrinho_page.verifica_item_carrinho(produto_1)
        carrinho_page.clicar_continuar_comprando()

        home_page.adicionar_item_carrinho("produto_2")

        home_page.acessa_carrinho()
        carrinho_page.verifica_item_carrinho(produto_1)
        carrinho_page.verifica_item_carrinho(produto_2)
