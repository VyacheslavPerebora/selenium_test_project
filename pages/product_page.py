from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item_to_basket(self):
        item_add = self.browser.find_element(*ProductPageLocators.BASKET_ICON)
        item_add.click()

    def should_be_message_about_added_item_and_match_names(self):
        """Проверяем наличие элемента с сообщением, что товар добавлен к корзину"""
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_TO_BASKET), 'Message about adding is not presented'
        # Находим элемент и переводим сообщение в текст
        message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_BASKET).text
        # Находим элемент и переводим название товара в текст
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # Проверяем, что название товара в сообщении совпадает с товаром, который мы добавили
        assert product_name.lower() == message.lower(), 'There is no such product in the message'

    def should_be_message_with_basket_cost_and_match_prices(self):
        """Проверяем наличие элемента с сообщением о стоимости товара"""
        assert self.is_element_present(*ProductPageLocators.BASKET_VALUE), 'Cart value not shown'
        # Находим элемент с ценой в сообщении и переводим в текст
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        # Находим элемент с ценой товара и переводим в текст
        cost_of_good = self.browser.find_element(*ProductPageLocators.COST_OF_ITEM).text
        # Проверяем, что цена товара совпадает с ценой в сообщении
        assert cost_of_good == basket_value, 'The price of the cart does not match the price of the product'

    def should_not_be_success_message_el_must_not_appeared(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_el_must_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"








