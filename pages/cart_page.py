import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Страница корзины"""
    
    # Локаторы
    CART_TABLE = (By.CSS_SELECTOR, "div.table-responsive")
    PRODUCT_ROW = (By.CSS_SELECTOR, "tbody tr")
    PRODUCT_NAME = (By.CSS_SELECTOR, "td.text-left a")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, "td.text-left input")
    UNIT_PRICE = (By.CSS_SELECTOR, "td.text-right:nth-child(5)")
    TOTAL_PRICE = (By.CSS_SELECTOR, "td.text-right:nth-child(6)")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.btn-danger")
    UPDATE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div#content p")
    CART_TOTAL = (By.CSS_SELECTOR, "td strong")
    
    @allure.step("Получить все товары в корзине")
    def get_cart_items(self):
        """Получить список всех товаров в корзине"""
        rows = self.find_elements(self.PRODUCT_ROW)
        items = []
        for row in rows:
            name = row.find_element(By.CSS_SELECTOR, "td.text-left a").text
            items.append(name)
        return items
    
    @allure.step("Удалить товар из корзины")
    def remove_first_item(self):
        """Удалить первый товар из корзины"""
        remove_buttons = self.find_elements(self.REMOVE_BUTTON)
        if remove_buttons:
            remove_buttons[0].click()
        return self
    
    @allure.step("Обновить количество товара: {quantity}")
    def update_quantity(self, quantity):
        """Обновить количество первого товара"""
        quantity_input = self.find_element(self.PRODUCT_QUANTITY)
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))
        self.click(self.UPDATE_BUTTON)
        return self
    
    @allure.step("Получить сообщение о пустой корзине")
    def get_empty_cart_message(self):
        """Получить сообщение, что корзина пуста"""
        if self.is_element_visible(self.EMPTY_CART_MESSAGE):
            return self.get_text(self.EMPTY_CART_MESSAGE)
        return ""
    
    @allure.step("Перейти к оформлению заказа")
    def proceed_to_checkout(self):
        """Нажать кнопку Checkout"""
        self.click(self.CHECKOUT_BUTTON)
        return self
    
    @allure.step("Получить общую стоимость корзины")
    def get_cart_total(self):
        """Получить общую сумму корзины"""
        total_text = self.get_text(self.CART_TOTAL)
        return total_text