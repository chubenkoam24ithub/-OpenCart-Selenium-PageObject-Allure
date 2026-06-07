import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Базовый класс для всех PageObject"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=0.5)
    
    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        """Открыть указанный URL"""
        self.driver.get(url)
        return self
    
    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        """Найти один элемент"""
        return self.driver.find_element(*locator)
    
    @allure.step("Найти все элементы: {locator}")
    def find_elements(self, locator):
        """Найти все элементы"""
        return self.driver.find_elements(*locator)
    
    @allure.step("Кликнуть на элемент: {locator}")
    def click(self, locator):
        """Кликнуть на элемент с ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self
    
    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def input_text(self, locator, text):
        """Очистить поле и ввести текст"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return self
    
    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        """Получить текст элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    @allure.step("Получить значение атрибута '{attribute}' элемента: {locator}")
    def get_attribute(self, locator, attribute):
        """Получить значение атрибута элемента"""
        return self.find_element(locator).get_attribute(attribute)
    
    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator):
        """Проверить, видим ли элемент"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    @allure.step("Проверить наличие элемента: {locator}")
    def is_element_present(self, locator):
        """Проверить, присутствует ли элемент в DOM"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    @allure.step("Сделать скриншот")
    def take_screenshot(self, name):
        """Сделать скриншот и прикрепить к Allure"""
        screenshot_path = f"screenshots/{name}.png"
        self.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)
        return screenshot_path