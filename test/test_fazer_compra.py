import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestFazerCompra():
    def test_cazer_compra(self):
        driver = conftest.driver
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()

        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()

        driver.find_element(By.ID,"add-to-cart").click()
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        driver.find_element(By.ID,"checkout").click()
        driver.find_element(By.ID,"first-name").send_keys("Teste")
        driver.find_element(By.ID,"last-name").send_keys("Teste")
        driver.find_element(By.ID,"postal-code").send_keys("99999999")
        driver.find_element(By.ID,"continue").click()

        assert driver.find_element(By.XPATH, "//*[@class='title']").is_displayed()

        driver.find_element(By.ID,"finish").click()

        assert driver.find_element(By.XPATH, "//*[@class='complete-header']").is_displayed()