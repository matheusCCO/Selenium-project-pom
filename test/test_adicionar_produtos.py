import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestAddProduto():
    def test_add_produto(self):
        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.procura_item()

        #driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()

        # driver.find_element(By.ID,"add-to-cart").click()
        # driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # driver.find_element(By.ID, "continue-shopping").click()

        # driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
        # driver.find_element(By.ID,"add-to-cart").click()

        # driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
