import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации"""

    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    # Универсальный локатор для ошибки в OpenCart 4
    LOGIN_ERROR = (By.CSS_SELECTOR, ".alert-danger, .alert.alert-danger")
    
    # Проверка успешного входа
    ACCOUNT_TITLE = (By.XPATH, "//h2[contains(text(),'My Account')]")

    @allure.step("Авторизоваться с email: {email}")
    def login(self, email, password):
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        btn = self.driver.find_element(*self.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn)
        return self

    @allure.step("Проверить, что вход выполнен успешно")
    def is_login_successful(self):
        """Проверяет появление заголовка 'My Account' или изменение URL"""
        try:
            # Ждём появления заголовка аккаунта
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ACCOUNT_TITLE)
            )
            return True
        except:
            # Альтернативная проверка по URL
            current_url = self.driver.current_url
            if "route=account/account" in current_url or "/account" in current_url:
                return True
            return False

    @allure.step("Получить сообщение об ошибке авторизации")
    def get_login_error_message(self):
        """Дожидается появления ошибки и возвращает её текст"""
        try:
            error = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.LOGIN_ERROR)
            )
            return error.text
        except:
            return ""
    @allure.step("Перейти на страницу восстановления пароля")
def go_to_forgotten_password(self):
    """Клик по ссылке 'Forgotten Password'"""
    self.click(self.FORGOTTEN_PASSWORD)
    return self

@allure.step("Запросить сброс пароля для email: {email}")
def request_password_reset(self, email):
    """Ввести email и отправить запрос на сброс"""
    email_input = (By.ID, "input-email")  # на странице forgotten пароль тоже есть поле email
    self.input_text(email_input, email)
    submit_button = (By.CSS_SELECTOR, "button[type='submit']")
    self.click(submit_button)
    return self

@allure.step("Получить сообщение об успешном запросе сброса")
def get_password_reset_success_message(self):
    """Текст сообщения после отправки запроса"""
    success_locator = (By.CSS_SELECTOR, ".alert-success")
    if self.is_element_visible(success_locator):
        return self.get_text(success_locator)
    return ""