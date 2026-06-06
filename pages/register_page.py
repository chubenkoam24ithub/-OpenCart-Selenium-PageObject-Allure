import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Страница регистрации"""
    
    # Локаторы
    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM = (By.ID, "input-confirm")
    AGREE = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#content h1")
    ACCOUNT_CREATED_TEXT = "Your Account Has Been Created!"
    
    # Сообщения об ошибках
    FIRSTNAME_ERROR = (By.CSS_SELECTOR, "input#input-firstname + div")
    LASTNAME_ERROR = (By.CSS_SELECTOR, "input#input-lastname + div")
    EMAIL_ERROR = (By.CSS_SELECTOR, "input#input-email + div")
    TELEPHONE_ERROR = (By.CSS_SELECTOR, "input#input-telephone + div")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "input#input-password + div")
    AGREE_ERROR = (By.CSS_SELECTOR, "div.alert-danger")
    
    @allure.step("Заполнить форму регистрации")
    def register_user(self, firstname, lastname, email, telephone, password, agree=True):
        """Заполнить и отправить форму регистрации"""
        self.input_text(self.FIRSTNAME, firstname)
        self.input_text(self.LASTNAME, lastname)
        self.input_text(self.EMAIL, email)
        self.input_text(self.TELEPHONE, telephone)
        self.input_text(self.PASSWORD, password)
        self.input_text(self.CONFIRM, password)
        
        if agree:
            self.click(self.AGREE)
        
        return self
    
    @allure.step("Нажать кнопку Continue")
    def submit_registration(self):
        """Отправить форму регистрации"""
        self.click(self.CONTINUE_BUTTON)
        return self
    
    @allure.step("Получить сообщение об успешной регистрации")
    def get_success_message(self):
        """Получить текст сообщения об успехе"""
        return self.get_text(self.SUCCESS_MESSAGE)
    
    @allure.step("Проверить, что регистрация успешна")
    def is_registration_successful(self):
        """Проверить, что регистрация прошла успешно"""
        return self.is_element_visible(self.SUCCESS_MESSAGE)
    
    @allure.step("Получить ошибку поля First Name")
    def get_firstname_error(self):
        """Получить текст ошибки для поля First Name"""
        if self.is_element_visible(self.FIRSTNAME_ERROR):
            return self.get_text(self.FIRSTNAME_ERROR)
        return ""
    
    @allure.step("Получить ошибку поля Email")
    def get_email_error(self):
        """Получить текст ошибки для поля Email"""
        if self.is_element_visible(self.EMAIL_ERROR):
            return self.get_text(self.EMAIL_ERROR)
        return ""