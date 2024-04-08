from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_form(self):
        '''Verifies login form is displayed'''
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing"
        assert True
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        '''Verifies correct login url is opened'''
        assert 'login' in self.browser.current_url, '"login" is missing in current url'
        assert True

    def should_be_register_form(self):
        '''Verifies registration form is displayed'''
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is missing"
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT).click()