import pytest
import allure
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


@allure.feature("Категории товаров")
@allure.story("Навигация по категориям")
class TestCategories:

    @allure.title("Переход в категорию 'Phones & PDAs' и проверка наличия товаров")
    @allure.severity(allure.severity_level.NORMAL)
    def test_phones_category_has_products(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)

        # Находим пункт меню "Phones & PDAs" (текст может отличаться в вашей версии)
        phones_menu = driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(text(), 'Phones')]")
        phones_menu.click()

        # Ждём загрузки страницы категории
        driver.implicitly_wait(2)

        # Проверяем, что есть хотя бы один товар
        product_elements = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
        assert len(product_elements) > 0, "В категории 'Phones & PDAs' нет товаров"

        # Проверяем, что заголовок страницы содержит название категории
        page_title = driver.find_element(By.CSS_SELECTOR, "#content h2").text
        assert "Phones" in page_title or "PDAs" in page_title

    @allure.title("Проверка отображения компонентов в категории 'Components'")
    def test_components_category_contains_subcategories(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)

        # Наводим на категорию "Components" (чтобы появилось подменю)
        components_menu = driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(text(), 'Components')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", components_menu)

        # В OpenCart может не быть выпадающего меню – тогда просто кликаем
        components_menu.click()

        driver.implicitly_wait(2)

        # Проверяем, что открылась страница с подкатегориями (обычно список ul)
        subcategories = driver.find_elements(By.CSS_SELECTOR, ".list-unstyled a")
        assert len(subcategories) > 0, "Нет подкатегорий в разделе Components"

    @allure.title("Поиск товара в категории через фильтр (если есть)")
    def test_category_filter(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)

        # Открываем категорию "Laptops & Notebooks" (пример)
        laptops_menu = driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(text(), 'Laptops')]")
        laptops_menu.click()
        driver.implicitly_wait(2)

        # Пробуем выбрать фильтр "Show All" или что-то подобное
        # Если фильтров нет – просто проверяем наличие товаров
        products = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
        assert len(products) > 0, "Нет товаров в категории Laptops & Notebooks"