import pytest
import allure
from pages.home_page import HomePage


@allure.feature("Настройки")
@allure.story("Смена валюты")
class TestCurrency:
    
    @allure.title("Смена валюты на EUR")
    @allure.severity(allure.severity_level.MINOR)
    def test_change_currency_to_eur(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        home.change_currency(home.CURRENCY_EUR)
        
        # Проверяем, что цена отображается в евро
        price_element = (By.CSS_SELECTOR, "p.price")
        assert home.is_element_visible(price_element)
    
    @allure.title("Смена валюты на GBP")
    def test_change_currency_to_gbp(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        home.change_currency(home.CURRENCY_GBP)
        
        price_element = (By.CSS_SELECTOR, "p.price")
        assert home.is_element_visible(price_element)