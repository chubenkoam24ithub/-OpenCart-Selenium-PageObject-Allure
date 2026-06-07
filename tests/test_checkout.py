import pytest
import allure
import random
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.product_page import ProductPage  # Явно импортируем класс

@allure.feature("Оформление заказа")
@allure.story("Checkout процесс")
class TestCheckout:
    
    @allure.title("Оформление заказа авторизованным пользователем")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_as_logged_in_user(self, driver, base_url):
        # 1. Создаём пользователя
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
        
        # 2. Добавляем товар
        # Переходим на главную
        home.open_home(base_url)
        
        # Выполняем поиск
        home.search("MacBook")
        
        # Находим первый товар в выдаче через стандартный CSS и кликаем
        first_product = driver.find_element(By.CSS_SELECTOR, "div.product-thumb h4 a")
        driver.execute_script("arguments[0].click();", first_product)
        
        # Теперь явно создаем объект страницы товара
        product_page = ProductPage(driver)
        product_page.add_to_cart()
        
        # 3. Переходим к оформлению
        driver.get(f"{base_url}/index.php?route=checkout/checkout")
        
        # 4. Проверка
        assert "Checkout" in driver.title or "checkout" in driver.current_url