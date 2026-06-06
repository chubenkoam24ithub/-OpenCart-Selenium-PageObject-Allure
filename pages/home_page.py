import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """Главная страница OpenCart"""
    
    # Локаторы
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn-default")
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, "a.dropdown-toggle")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    CART_BUTTON = (By.CSS_SELECTOR, "a.btn-lg")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "button.dropdown-toggle")
    CURRENCY_EUR = (By.NAME, "EUR")
    CURRENCY_GBP = (By.NAME, "GBP")
    CURRENCY_USD = (By.NAME, "USD")
    PRODUCT_LINK = (By.CSS_SELECTOR, "div.product-thumb h4 a")
    
    @allure.step("Открыть главную страницу")
    def open_home(self, base_url):
        self.open(base_url)
        return self
    
    @allure.step("Поиск товара: {keyword}")
    def search(self, keyword):
        """Выполнить поиск товара"""
        self.input_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)
        from pages.product_page import ProductPage
        return ProductPage(self.driver)
    
    @allure.step("Перейти на страницу регистрации")
    def go_to_register(self):
        """Перейти на страницу регистрации"""
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.REGISTER_LINK)
        from pages.register_page import RegisterPage
        return RegisterPage(self.driver)
    
    @allure.step("Перейти на страницу логина")
    def go_to_login(self):
        """Перейти на страницу авторизации"""
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.LOGIN_LINK)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)
    
    @allure.step("Сменить валюту на {currency}")
    def change_currency(self, currency_locator):
        """Сменить валюту"""
        self.click(self.CURRENCY_DROPDOWN)
        self.click(currency_locator)
        return self
    
    @allure.step("Кликнуть на первый товар")
    def click_first_product(self):
        """Кликнуть на первый товар в каталоге"""
        self.click(self.PRODUCT_LINK)
        from pages.product_page import ProductPage
        return ProductPage(self.driver)