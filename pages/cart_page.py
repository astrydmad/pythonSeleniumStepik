from .base_page import BasePage
from .locators import CartLocators


class CartPage(BasePage):
    def should_be_message_that_cart_is_empty(self):
        '''Verifies cart has a message when no products are added in the cart'''
        assert self.is_element_present(*CartLocators.EMPTY_CART_MESSAGE), "The product is displayed in cart"

    def should_not_be_items(self):
        '''Verifies there're no items in cart'''
        self.is_not_element_present(*CartLocators.CART_ITEMS), "Items are added in cart"
