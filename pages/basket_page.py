from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_item_in_basket(self):
        """Проверяем, что товар добавлен в корзину"""
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), 'Basket is not empty, but should be'

    def should_be_message_basket_empty(self):
        """Проверяем, что корзина пуста, позитивная и негативная проверки"""
        message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        assert message, 'Message "basket_empty" is not exist, but should be'


