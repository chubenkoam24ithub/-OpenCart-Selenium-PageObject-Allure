import pytest
import allure
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


@allure.feature("Настройки")
@allure.story("Смена валюты")
class TestCurrency:

    @allure.title("Смена валюты на EUR")
    @allure.severity(allure.severity_level.MINOR)
    def test_change_currency_to_eur(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)

        # Кликаем по кнопке/ссылке выбора валюты (обычно это элемент с id="form-currency")
        currency_selector = driver.find_element(By.ID, "form-currency")
        currency_selector.click()

        # Ищем элемент, который содержит текст "EUR" или "€" (без учёта регистра)
        eur_option = driver.find_element(By.XPATH, "//*[contains(text(), 'EUR') or contains(text(), '€')]")
        eur_option.click()

        driver.implicitly_wait(2)

        # Проверяем, что символ евро появился на странице
        assert "€" in driver.page_source or "EUR" in driver.page_source

    @allure.title("Смена валюты на GBP")
    def test_change_currency_to_gbp(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)

        currency_selector = driver.find_element(By.ID, "form-currency")
        currency_selector.click()

        gbp_option = driver.find_element(By.XPATH, "//*[contains(text(), 'GBP') or contains(text(), '£')]")
        gbp_option.click()

        driver.implicitly_wait(2)

        assert "£" in driver.page_source or "GBP" in driver.page_source