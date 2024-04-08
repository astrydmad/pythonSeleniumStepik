from .base_page import BasePage
# from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math
import re
import time
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_item_to_cart(self):
        '''Cliks "Add to cart" button'''
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_product_button.click()

    def get_name_of_product_was_added_to_cart(self):
        '''Returns the name of added product'''
        return self.browser.find_element(*ProductPageLocators.PRODUCT_WAS_ADDED_TO_CART).text
    
    def get_product_name(self):
        '''Returns product name'''
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        '''Returns product price'''
        msg = self.browser.find_element(*ProductPageLocators.PRICE).text
        return float(re.search(r'\d{2}[.,]\d{2}', msg).group(0).replace(',', '.')) if msg else 0
    
    def get_total_cart_price(self):
        '''Returns total cart price'''
        msg = self.browser.find_element(*ProductPageLocators.CART_SUM).text
        return float(re.search(r'\d{2}[.,]\d{2}', msg).group(0).replace(',', '.')) if msg else None if msg else 0
    
    def should_be_add_to_cart_button(self):
        '''Verifies "Add to cart" button is present'''
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Button is missing"

    def should_be_cart_sum(self):
        '''Verifies added to cart sum'''
        return self.is_element_present(*ProductPageLocators.CART_SUM), 'Cart sum is missing'
    
    def should_be_increased_price_basket(self):
        '''Price in basket changed'''
        product_price = self.get_product_price()
        total_price = self.get_total_cart_price()
        assert product_price == total_price, 'Cart price and product price do not match. Product: {}. Cart: {}'.format(
            product_price, total_price)
        
    def should_be_msg_product_added_to_cart(self):
        '''Verifies product is added to cart message'''
        return self.is_element_present(*ProductPageLocators.PRODUCT_WAS_ADDED_TO_CART), 'Product is added to cart message is missing'
    
    def should_exact_product_added_to_cart(self):
        '''Verifies the exact product is added to cart'''
        assert self.get_product_name() == self.get_name_of_product_was_added_to_cart(), 'Invalid product is added to cart'

    def should_be_product_name(self):
        '''Verifies product name is present'''
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Product name is missing'

    def should_be_product_price(self):
        '''Verifies product price is present'''
        assert self.is_element_present(*ProductPageLocators.PRICE), 'Product price is missing'
    
    def should_be_removed_success_message(self):
        '''Verifies Success message was removed'''
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message did not disappear"

    def should_not_be_success_message(self):
        '''Verifies there's no Success message'''
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is displayed"

    def solve_quiz_and_get_code(self):
        '''Solves the task and pastes the solution'''
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            time.sleep(5)
            print(f"Your code: {alert_text}")
            time.sleep(5)
            alert.accept()
            time.sleep(1)
        except NoAlertPresentException:
            print("No second alert presented")

    def test_guest_cant_see_success_message(self):
        '''Success message is not displayed for guest user when opens the product page'''
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is displayed"
        
    def test_message_disappeared_after_adding_product_to_basket(self):
        '''Verifies Success message was removed'''
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message did not disappear"