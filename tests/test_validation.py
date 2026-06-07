import pytest
import allure
from pages.home_page import HomePage


@allure.feature("Валидация")
@allure.story("Проверка полей ввода")
class TestValidation:
    
    @allure.title("Валидация поля Email в регистрации")
    @allure.severity(allure.severity_level.NORMAL)
    def test_email_validation(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        register = home.go_to_register()
        
        register.register_user(
            firstname="Test",
            lastname="User",
            email="invalid-email", # Некорректный email
            password="Password123!"
        ).submit_registration()
        
        # Если валидация работает, мы остались на той же странице (URL содержит route=account/register)
        assert "route=account/register" in driver.current_url or "register" in driver.current_url
    
    @allure.title("Валидация поля Password (минимальная длина)")
    def test_password_min_length_validation(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        register = home.go_to_register()
        
        register.register_user(
            firstname="Test",
            lastname="User",
            email="valid@example.com",
            password="123" # Слишком короткий пароль
        ).submit_registration()
        
        # Проверяем, что нас не пустило дальше страницы регистрации
        assert "route=account/register" in driver.current_url or "register" in driver.current_url