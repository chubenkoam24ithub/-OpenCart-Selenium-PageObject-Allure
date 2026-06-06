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
        
        # Делаем скриншот и прикрепляем к Allure
        home.take_screenshot("homepage")
        
        # Проверяем, что элемент виден
        logo = (By.CSS_SELECTOR, "img[title='Your Store']")
        assert home.is_element_visible(logo)
    
    @allure.title("Скриншот страницы товара")
    def test_screenshot_of_product_page(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        product_page = home.search("MacBook")
        product_page.take_screenshot("product_page")
        
        assert "MacBook" in product_page.get_product_name()