import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class ValidaPedido(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name']")

    def verifica_informacao_pedido(self):
        self.verifca_elementos_existe(self.item_inventario)
        #assert len(self.encontar_elementos(self.item_inventario)) >0, f"'{self.item_inventario}' não encontrou nem um item"