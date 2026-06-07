import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """Главная страница OpenCart"""
    
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//span[contains(text(), 'My Account')]/..")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")  # <-- ДОБАВИТЬ ЭТУ СТРОКУ
    
    @allure.step("Открыть главную страницу")
    def open_home(self, base_url):
        self.open(base_url)
        return self
    
    @allure.step("Поиск товара: {keyword}")
    def search(self, keyword):
        self.input_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)
        return self
    
    @allure.step("Перейти на страницу регистрации")
    def go_to_register(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.REGISTER_LINK)
        from pages.register_page import RegisterPage
        return RegisterPage(self.driver)
    
    @allure.step("Перейти на страницу логина")
    def go_to_login(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.LOGIN_LINK)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)
    
    @allure.step("Выйти из аккаунта")
    def logout(self):
        """Выход из учётной записи, если пользователь авторизован"""
        # Сначала открываем выпадающее меню
        self.click(self.MY_ACCOUNT_DROPDOWN)
        # Кликаем по ссылке Logout
        self.click(self.LOGOUT_LINK)
        return self