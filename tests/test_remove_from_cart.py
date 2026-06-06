import pytest
import allure
from pages.home_page import HomePage
from pages.cart_page import CartPage


@allure.feature("Корзина")
@allure.story("Удаление товаров")
class TestRemoveFromCart:
    
    @allure.title("Удаление товара из корзины")
    @allure.severity(allure.severity_level.NORMAL)
    def test_remove_product_from_cart(self, driver, base_url):
        # Сначала добавим товар
        home = HomePage(driver)
        home.open_home(base_url)
        product_page = home.search("MacBook")
        product_page.add_to_cart()
        
        # Переходим в корзину
        driver.get(f"{base_url}/index.php?route=checkout/cart")
        cart_page = CartPage(driver)
        
        # Удаляем товар
        cart_page.remove_first_item()
        
        # Проверяем, что корзина пуста
        empty_message = cart_page.get_empty_cart_message()
        assert "Your shopping cart is empty!" in empty_message