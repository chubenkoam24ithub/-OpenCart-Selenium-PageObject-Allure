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
        
        # Вводим некорректный email
        register.register_user(
            firstname="Test",
            lastname="User",
            email="invalid-email",
            telephone="123456789",
            password="Password123!"
        ).submit_registration()
        
        email_error = register.get_email_error()
        # Должна быть ошибка валидации
        assert email_error != "" or register.is_element_visible(register.EMAIL_ERROR)
    
    @allure.title("Валидация поля Password (минимальная длина)")
    def test_password_min_length_validation(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        register = home.go_to_register()
        
        # Вводим слишком короткий пароль
        register.register_user(
            firstname="Test",
            lastname="User",
            email="valid@example.com",
            telephone="123456789",
            password="123"
        ).submit_registration()
        
        # Должна появиться ошибка о длине пароля
        assert register.is_element_visible(register.PASSWORD_ERROR)