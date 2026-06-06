import pytest
import allure
import random
from pages.home_page import HomePage


@allure.feature("Авторизация")
@allure.story("Вход в аккаунт")
class TestLogin:
    
    @allure.title("Успешный вход с валидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, driver, base_url):
        # Сначала создадим пользователя
        home = HomePage(driver)
        home.open_home(base_url)
        
        unique_email = f"logintest{random.randint(100000, 999999)}@example.com"
        
        register = home.go_to_register()
        register.register_user(
            firstname="Login",
            lastname="Test",
            email=unique_email,
            telephone="79991234567",
            password="Password123!"
        ).submit_registration()
        
        assert register.is_registration_successful()
        
        # Теперь логинимся
        home = HomePage(driver)
        home.open_home(base_url)
        login_page = home.go_to_login()
        login_page.login(unique_email, "Password123!")
        
        assert login_page.is_login_successful()
    
    @allure.title("Вход с неверным паролем")
    def test_login_invalid_password(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        login_page = home.go_to_login()
        login_page.login("nonexistent@example.com", "WrongPassword")
        
        error_message = login_page.get_login_error_message()
        assert "Warning: No match" in error_message or "No match" in error_message