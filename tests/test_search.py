import pytest
import allure
from pages.home_page import HomePage


@allure.feature("Поиск")
@allure.story("Поиск товаров")
class TestSearch:
    
    @allure.title("Поиск существующего товара")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_existing_product(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        product_page = home.search("iPhone")
        
        assert product_page.is_element_visible(product_page.PRODUCT_NAME)
        product_name = product_page.get_product_name()
        assert "iPhone" in product_name
    
    @allure.title("Поиск несуществующего товара")
    def test_search_nonexistent_product(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        product_page = home.search("NonexistentProductXYZ123")
        
        # Проверяем сообщение "нет результатов"
        empty_result = (By.CSS_SELECTOR, "div#content p")
        assert product_page.is_element_visible(empty_result)