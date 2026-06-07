import pytest
import allure
from pages.home_page import HomePage


@allure.feature("Скриншоты")
@allure.story("Визуальная проверка")
class TestScreenshot:
    
    @allure.title("Скриншот главной страницы")
    @allure.severity(allure.severity_level.MINOR)
    def test_screenshot_of_homepage(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        # Делаем скриншот
        home.take_screenshot("homepage")
        
        # Просто проверяем, что страница загрузилась
        assert "Your Store" in driver.title or "OpenCart" in driver.title
    
    @allure.title("Скриншот страницы после поиска")
    def test_screenshot_of_product_page(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        home.search("MacBook")
        
        home.take_screenshot("search_results")
        
        assert "MacBook" in driver.page_source