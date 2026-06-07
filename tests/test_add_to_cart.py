import pytest
import allure
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


@allure.feature("Корзина")
@allure.story("Добавление товаров")
class TestAddToCart:

    @allure.title("Добавление товара в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product_to_cart(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        home.search("MacBook")

        # Находим ссылку на первый товар в результатах поиска
        first_product = driver.find_element(By.CSS_SELECTOR, ".product-thumb h4 a")
        # Прокручиваем к элементу
        driver.execute_script("arguments[0].scrollIntoView(true);", first_product)
        driver.implicitly_wait(1)
        # Кликаем через JavaScript (обходит перехват)
        driver.execute_script("arguments[0].click();", first_product)

        # Ждём загрузки страницы товара
        driver.implicitly_wait(3)

        # Добавляем товар в корзину
        add_to_cart_button = driver.find_element(By.ID, "button-cart")
        add_to_cart_button.click()

        # Проверяем успех
        assert "Success" in driver.page_source or "success" in driver.page_source.lower()

    @allure.title("Добавление товара с изменением количества")
    def test_add_product_with_quantity(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        home.search("iPhone")

        first_product = driver.find_element(By.CSS_SELECTOR, ".product-thumb h4 a")
        driver.execute_script("arguments[0].scrollIntoView(true);", first_product)
        driver.implicitly_wait(1)
        driver.execute_script("arguments[0].click();", first_product)

        driver.implicitly_wait(3)

        # Меняем количество
        quantity_input = driver.find_element(By.ID, "input-quantity")
        quantity_input.clear()
        quantity_input.send_keys("3")

        # Добавляем в корзину
        add_to_cart_button = driver.find_element(By.ID, "button-cart")
        add_to_cart_button.click()

        assert "Success" in driver.page_source or "success" in driver.page_source.lower()