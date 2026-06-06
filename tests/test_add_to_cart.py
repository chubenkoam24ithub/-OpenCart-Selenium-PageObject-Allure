import pytest
import allure
from pages.home_page import HomePage


@allure.feature("Корзина")
@allure.story("Добавление товаров")
class TestAddToCart:
    
    @allure.title("Добавление товара в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product_to_cart(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        # Ищем и открываем товар
        product_page = home.search("MacBook")
        
        # Добавляем в корзину
        product_page.add_to_cart()
        
        # Проверяем сообщение об успехе
        success_msg = product_page.get_success_message()
        assert "Success: You have added" in success_msg
    
    @allure.title("Добавление товара с изменением количества")
    def test_add_product_with_quantity(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        product_page = home.search("iPhone")
        product_page.add_to_cart(quantity=3)
        
        success_msg = product_page.get_success_message()
        assert "Success: You have added" in success_msg