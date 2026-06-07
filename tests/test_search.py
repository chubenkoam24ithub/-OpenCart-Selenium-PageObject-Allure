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
        home.search("MacBook")
        
        # Проверяем, что на странице есть слово MacBook
        assert "MacBook" in driver.page_source
    
    @allure.title("Поиск несуществующего товара")
    def test_search_nonexistent_product(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        home.search("NonexistentProductXYZ123")
        
        # Проверяем сообщение "нет результатов"
        assert "There is no product that matches the search criteria" in driver.page_source