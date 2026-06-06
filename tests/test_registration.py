import pytest
import allure
import random
from pages.home_page import HomePage


@allure.feature("Регистрация")
@allure.story("Создание нового аккаунта")
class TestRegistration:
    
    @allure.title("Успешная регистрация нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_registration(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        register = home.go_to_register()
        
        # Генерация уникального email
        unique_email = f"testuser{random.randint(100000, 999999)}@example.com"
        
        register.register_user(
            firstname="Тест",
            lastname="Тестов",
            email=unique_email,
            telephone="79991234567",
            password="Password123!"
        ).submit_registration()
        
        assert register.is_registration_successful()
        assert register.get_success_message() == "Your Account Has Been Created!"
    
    @allure.title("Регистрация с уже существующим email")
    def test_registration_duplicate_email(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        register = home.go_to_register()
        
        register.register_user(
            firstname="Тест",
            lastname="Тестов",
            email="existing@example.com",
            telephone="79991234567",
            password="Password123!"
        ).submit_registration()
        
        # Должна появиться ошибка о существующем email
        error_text = register.get_email_error()
        assert "already registered" in error_text or "E-Mail" in error_text
    
    @allure.title("Регистрация без обязательных полей")
    def test_registration_missing_required_fields(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        register = home.go_to_register()
        
        # Отправляем пустую форму
        register.submit_registration()
        
        # Проверяем наличие ошибок
        firstname_error = register.get_firstname_error()
        assert firstname_error != "", "Должна быть ошибка для First Name"