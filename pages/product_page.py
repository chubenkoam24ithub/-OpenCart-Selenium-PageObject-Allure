import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    """Страница товара"""
    
    # Локаторы
    PRODUCT_NAME = (By.CSS_SELECTOR, "div#content h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span.price-new, li.price")
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    QUANTITY_INPUT = (By.ID, "input-quantity")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")
    COMPARE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Compare this Product']")
    RATING_STARS = (By.CSS_SELECTOR, "div.rating")
    DESCRIPTION_TAB = (By.LINK_TEXT, "Description")
    DESCRIPTION_TEXT = (By.CSS_SELECTOR, "div#tab-description")
    
    @allure.step("Получить название товара")
    def get_product_name(self):
        """Получить название текущего товара"""
        return self.get_text(self.PRODUCT_NAME)
    
    @allure.step("Получить цену товара")
    def get_product_price(self):
        """Получить цену текущего товара"""
        return self.get_text(self.PRODUCT_PRICE)
    
    @allure.step("Добавить товар в корзину (количество: {quantity})")
    def add_to_cart(self, quantity=1):
        """Добавить товар в корзину с указанным количеством"""
        if quantity != 1:
            self.input_text(self.QUANTITY_INPUT, str(quantity))
        self.click(self.ADD_TO_CART_BUTTON)
        return self
    
    @allure.step("Получить сообщение о добавлении в корзину")
    def get_success_message(self):
        """Получить сообщение об успешном добавлении"""
        if self.is_element_visible(self.SUCCESS_MESSAGE):
            return self.get_text(self.SUCCESS_MESSAGE)
        return ""
    
    @allure.step("Добавить товар в список желаний")
    def add_to_wishlist(self):
        """Добавить товар в вишлист"""
        self.click(self.WISHLIST_BUTTON)
        return self
    
    @allure.step("Добавить товар к сравнению")
    def add_to_compare(self):
        """Добавить товар для сравнения"""
        self.click(self.COMPARE_BUTTON)
        return self