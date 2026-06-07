import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


@allure.feature("Alert")
@allure.story("Работа с всплывающими окнами")
class TestAlert:
    
    @allure.title("Обработка alert (если есть на странице)")
    @allure.severity(allure.severity_level.MINOR)
    def test_alert_handling(self, driver, base_url):
        # На некоторых страницах OpenCart нет alert, поэтому тест демонстрационный
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        
        # Кликаем на кнопку, вызывающую alert
        alert_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
        alert_button.click()
        
        # Переключаемся на alert и принимаем его
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        
        assert alert_text == "I am a JS Alert"