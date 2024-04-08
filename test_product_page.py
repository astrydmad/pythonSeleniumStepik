# from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import CartPage
import time
import pytest

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    login_page = ProductPage(browser, browser.current_url)
    login_page.add_item_to_cart()

def test_guest_should_see_add_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_add_to_cart_button()
    page.add_item_to_cart()
    # page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_product_name()
    page.should_be_product_price()
    page.should_exact_product_added_to_cart()
    page.should_be_increased_price_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_message_that_cart_is_empty()
    cart_page.should_not_be_items()

class TestUserAddToBasketFromProductPage():
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    login_link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, self.login_link)
        page.open()
        email = str(time.time()) + "@fake-mail.org"
        page.register_new_user(email, 'test-password')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.test_guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_add_to_cart_button()
        page.add_item_to_cart()
        page.should_be_product_price()
        page.should_be_product_name()
        page.should_exact_product_added_to_cart()
        page.should_be_increased_price_basket()

    