import pytest
import allure
import random
from pages.home_page import HomePage


@allure.feature("Оформление заказа")
@allure.story("Checkout процесс")
class TestCheckout:
    
    @allure.title("Оформление заказа авторизованным пользователем")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_as_logged_in_user(self, driver, base_url):
        # Создаём пользователя
        home = HomePage(driver)
        home.open_home(base_url)
        
        unique_email = f"checkout{random.randint(100000, 999999)}@example.com"
        
        register = home.go_to_register()
        register.register_user(
            firstname="Checkout",
            lastname="Test",
            email=unique_email,
            telephone="79991234567",
            password="Password123!"
        ).submit_registration()
        
        # Добавляем товар
        home = HomePage(driver)
        home.open_home(base_url)
        product_page = home.search("MacBook")
        product_page.add_to_cart()
        
        # Переходим к оформлению
        driver.get(f"{base_url}/index.php?route=checkout/checkout")
        
        # Проверяем, что мы на странице оформления
        assert "Checkout" in driver.title