import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации"""
    
    # Локаторы
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    CONTINUE_BUTTON = (By.LINK_TEXT, "Continue")
    MY_ACCOUNT_TITLE = (By.CSS_SELECTOR, "div#content h2")
    LOGOUT_SUCCESS = (By.CSS_SELECTOR, "div#content h1")
    LOGIN_ERROR = (By.CSS_SELECTOR, "div.alert-danger")
    
    @allure.step("Авторизоваться с email: {email}")
    def login(self, email, password):
        """Выполнить вход в аккаунт"""
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self
    
    @allure.step("Получить заголовок страницы аккаунта")
    def get_my_account_title(self):
        """Получить заголовок 'My Account'"""
        return self.get_text(self.MY_ACCOUNT_TITLE)
    
    @allure.step("Проверить, что вход выполнен успешно")
    def is_login_successful(self):
        """Проверить, что пользователь авторизован"""
        return "My Account" in self.get_my_account_title()
    
    @allure.step("Получить сообщение об ошибке авторизации")
    def get_login_error_message(self):
        """Получить текст ошибки при неверных данных"""
        if self.is_element_visible(self.LOGIN_ERROR):
            return self.get_text(self.LOGIN_ERROR)
        return ""
    
    @allure.step("Перейти на страницу восстановления пароля")
    def go_to_forgotten_password(self):
        """Перейти на страницу восстановления пароля"""
        self.click(self.FORGOTTEN_PASSWORD)
        return self