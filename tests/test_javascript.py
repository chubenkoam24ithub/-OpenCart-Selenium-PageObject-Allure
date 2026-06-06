import pytest
import allure
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


@allure.feature("JavaScript")
@allure.story("Выполнение JS скриптов")
class TestJavaScript:
    
    @allure.title("Прокрутка страницы с помощью JS")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scroll_with_javascript(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        # Прокручиваем страницу вниз с помощью JS
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Проверяем, что футер виден
        footer = (By.CSS_SELECTOR, "footer")
        assert home.is_element_visible(footer)
    
    @allure.title("Изменение атрибута элемента через JS")
    def test_change_attribute_with_javascript(self, driver, base_url):
        home = HomePage(driver)
        home.open_home(base_url)
        
        search_input = home.find_element(home.SEARCH_INPUT)
        
        # Меняем атрибут через JS
        driver.execute_script("arguments[0].setAttribute('placeholder', 'Новый поиск');", search_input)
        
        new_placeholder = search_input.get_attribute("placeholder")
        assert new_placeholder == "Новый поиск"