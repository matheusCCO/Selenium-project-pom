import conftest

class BasePage:
    def __init__(self):
        self.driver = conftest
    
    def encontar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def escrever(self, locator, text):
        self.encontar_elemento(locator).send_keys(text)
    
    def clicar(self, locator):
        self.encontar_elemento(locator).click()
    
    def vefificar_se_elemento_existe(self, locator):
        assert self.encontar_elemento(locator).is_displayed(), f"O elemeto '{locator}' não foi encontrado na tela."

    def pegar_testo_elemento(self, locator):
        return self.encontar_elemento(locator).text
    
