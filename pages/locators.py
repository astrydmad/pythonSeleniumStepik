from selenium.webdriver.common.by import By

class BasePageLocators():
    CART_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini')] //a[contains(@class, 'btn-default')]")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "login_link1")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class CartLocators():
    ADD_TO_CART = (By.XPATH, "//button[@value='Add to basket']")
    CART_ITEMS = (By.CLASS_NAME, 'basket-items')
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[@id='content_inner']//*[contains(text(), 'Your basket is empty.')]")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "#id_login-login_submit")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_FORM = (By.ID, 'register_form')
    REG_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.XPATH, "//button[@name='registration_submit']")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_CART = (By.XPATH, "//button[@value='Add to basket']")
    CART_SUM = (By.CLASS_NAME, 'basket-mini')
    PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_WAS_ADDED_TO_CART = SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
