import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.preenche_informacao_pedido import PreencheInformacao
from pages.valida_informacao_pedido import ValidaPedido 

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestFazerCompra():
    def test_cazer_compra(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        informacao_pedido = PreencheInformacao()
        valida_pedido = ValidaPedido()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"
        nome="Lucas"
        sobrenome="Silva"
        cep= 99999999


        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.adicionar_item_carrinho(produto_1)
        home_page.voltar_para_home_page()

        home_page.adicionar_item_carrinho(produto_2)
        home_page.acessa_carrinho()

        carrinho_page.verifica_item_carrinho(produto_1)
        carrinho_page.verifica_item_carrinho(produto_2)
        carrinho_page.fazer_compar_item_carrinho()
        informacao_pedido.preenche_informacao(nome,sobrenome,cep)
        valida_pedido.verifica_informacao_pedido()
        



 
        # driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()

        # driver.find_element(By.ID,"add-to-cart").click()
        # driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # driver.find_element(By.ID,"checkout").click()
        # driver.find_element(By.ID,"first-name").send_keys("Teste")
        # driver.find_element(By.ID,"last-name").send_keys("Teste")
        # driver.find_element(By.ID,"postal-code").send_keys("99999999")
        # driver.find_element(By.ID,"continue").click()

        # assert driver.find_element(By.XPATH, "//*[@class='title']").is_displayed()

        # driver.find_element(By.ID,"finish").click()

        # assert driver.find_element(By.XPATH, "//*[@class='complete-header']").is_displayed()