import conftest
from pages.base_page import BasePage
from pages.login_page import By


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//*[@class='title']")
        self.item = (By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']")
        

    def verificar_login_sucesso(self):
        self.vefificar_se_elemento_existe(self.titulo_pagina)
    
    def procura_item(self):
        self.encontar_elemento(self.item)
        self.clicar(self.item)
