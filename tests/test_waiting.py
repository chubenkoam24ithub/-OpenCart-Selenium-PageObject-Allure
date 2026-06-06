import pytest
import allure
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


@allure.feature("Ожидания")
@allure.story("Проверка явных и неявных ожиданий")
class TestWaiting:
    
    @allure.title("Проверка появления элемента после загрузки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_element_appears_after_load(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        # Используем явное ожидание из BasePage
        logo = (By.CSS_SELECTOR, "img[title='Your Store']")
        assert home.is_element_visible(logo)
    
    @allure.title("Ожидание появления сообщения после действия")
    def test_success_message_appears(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        product_page = home.search("iPhone")
        product_page.add_to_cart()
        
        # Ждём появления сообщения об успехе
        success_locator = (By.CSS_SELECTOR, "div.alert-success")
        assert product_page.is_element_visible(success_locator)