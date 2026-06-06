import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
@allure.title("Инициализация и закрытие браузера")
def driver():
    options = Options()
    
    options.add_argument("--window-size=1280,800")
    options.add_argument("--disable-cache")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
  
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(5)  # Неявное ожидание
    
    yield driver
    
    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    return "http://localhost:8081"
