import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage


@allure.feature("Корзина")
@allure.story("Удаление товаров")
class TestRemoveFromCart:

    @allure.title("Удаление товара из корзины")
    @allure.severity(allure.severity_level.NORMAL)
    def test_remove_product_from_cart(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)

        # Добавляем товар
        home.search("MacBook")
        first_product = driver.find_element(By.CSS_SELECTOR, ".product-thumb h4 a")
        driver.execute_script("arguments[0].scrollIntoView(true);", first_product)
        driver.execute_script("arguments[0].click();", first_product)

        add_to_cart_button = driver.find_element(By.ID, "button-cart")
        add_to_cart_button.click()

        # Ждём появления сообщения об успешном добавлении
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))

        # Небольшая пауза для завершения AJAX
        driver.implicitly_wait(2)

        # Переходим в корзину
        driver.get(f"{base_url}/index.php?route=checkout/cart")

        # Ждём загрузки страницы корзины
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content")))

        # Проверяем, что корзина не пуста
        page_text = driver.find_element(By.CSS_SELECTOR, "#content").text
        if "Your shopping cart is empty" in page_text:
            # Если пусто — возможно, товар не добавился. Выведем отладочную информацию.
            pytest.fail("Корзина пуста после добавления товара. Возможно, не сработала кнопка 'Add to Cart'.")

        # Находим кнопку удаления (универсальный поиск)
        remove_button = driver.find_element(By.XPATH, "//table[@class='table table-bordered']//tbody//tr//td[last()]//button")
        remove_button.click()

        # Ждём обновления страницы и появления сообщения о пустой корзине
        wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'empty')]")))
        empty_text = driver.find_element(By.CSS_SELECTOR, "#content p").text
        assert "empty" in empty_text.lower()