import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Страница регистрации – поддержка OpenCart 3 и 4"""

    # Поля ввода
    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM = (By.ID, "input-confirm")
    AGREE = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Успех – заголовок после регистрации
    SUCCESS_TITLE = (By.CSS_SELECTOR, "#content h1")

    # Общий блок ошибок вверху (OC3/OC4)
    GENERAL_ALERT = (By.CSS_SELECTOR, ".alert-danger, .alert.alert-danger")

    # Ошибки под полями – комбинируем возможные селекторы
    # В OC4 используется class="text-danger", в OC3 – отдельный элемент с id="error-firstname"
    FIRSTNAME_ERROR = (By.CSS_SELECTOR, "#error-firstname, .text-danger, .invalid-feedback")
    LASTNAME_ERROR = (By.CSS_SELECTOR, "#error-lastname, .text-danger, .invalid-feedback")
    EMAIL_ERROR = (By.CSS_SELECTOR, "#error-email, .text-danger, .invalid-feedback")
    TELEPHONE_ERROR = (By.CSS_SELECTOR, "#error-telephone, .text-danger, .invalid-feedback")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "#error-password, .text-danger, .invalid-feedback")

    @allure.step("Заполнить форму регистрации")
    def register_user(self, firstname, lastname, email, password, telephone=None, agree=True):
        self.input_text(self.FIRSTNAME, firstname)
        self.input_text(self.LASTNAME, lastname)
        self.input_text(self.EMAIL, email)

        if telephone and self.is_element_present(self.TELEPHONE):
            self.input_text(self.TELEPHONE, telephone)

        self.input_text(self.PASSWORD, password)

        if self.is_element_present(self.CONFIRM):
            self.input_text(self.CONFIRM, password)

        if agree:
            agree_checkbox = self.driver.find_element(*self.AGREE)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", agree_checkbox)
            self.driver.execute_script("arguments[0].click();", agree_checkbox)

        return self

    @allure.step("Нажать кнопку Continue")
    def submit_registration(self):
        btn = self.driver.find_element(*self.CONTINUE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        # Даём время браузеру на обработку (для валидации OC4)
        time.sleep(1)
        return self

    @allure.step("Проверить, что регистрация успешна")
    def is_registration_successful(self):
        """Ожидаем появления заголовка успеха (старая страница заменяется новой)"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.SUCCESS_TITLE)
            )
            return True
        except:
            return False

    @allure.step("Получить сообщение об успешной регистрации")
    def get_success_message(self):
        if self.is_registration_successful():
            return self.get_text(self.SUCCESS_TITLE)
        return ""

    def _get_field_error_text(self, locator, field_name):
        """Внутренний метод: ищет ошибку под полем или в общем алерте"""
        # 1. Ошибка конкретно под полем
        if self.is_element_visible(locator):
            return self.get_text(locator)
        # 2. Общая ошибка (alert-danger) может содержать текст про это поле
        general = self.get_general_error_text()
        if general and field_name in general:
            return general
        # 3. В OC4 ошибки могут быть в data-атрибутах – пробуем найти элемент с классом is-invalid
        return ""

    @allure.step("Получить ошибку поля First Name")
    def get_firstname_error(self):
        return self._get_field_error_text(self.FIRSTNAME_ERROR, "First Name")

    @allure.step("Получить ошибку поля Email")
    def get_email_error(self):
        return self._get_field_error_text(self.EMAIL_ERROR, "E-Mail")

    @allure.step("Получить текст общей ошибки")
    def get_general_error_text(self):
        try:
            alert = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.GENERAL_ALERT)
            )
            return alert.text
        except:
            return ""