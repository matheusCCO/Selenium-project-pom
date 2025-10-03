import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLogin:
    def test_login_invalido(self):
        mensagem_erro_esperado= "Epic sadface: Username and password do not match any user in this service"
        login_page = LoginPage() #Instancia
        login_page.fazer_login("standard_user", "senha_incorreta") #Faz um login com senha errada
        login_page.verifcar_mansagem_erro_login_existe() #verifica se a mansagem de erro aparece.
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperado) #verifca o texto esperado
