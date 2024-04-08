from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_cart_page(self):
        '''User navigates to Cart page'''
        link = self.browser.find_element(*BasePageLocators.CART_LINK)
        link.click()

    def go_to_login_page(self):
        '''User navigates to Login page'''
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
    
    def is_disappeared(self, how, what, timeout=4):
        '''Verifies element is disappeared'''
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def is_element_present(self, how, what):
        '''Verifies element is present'''
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        '''Verifies element is not present'''
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        '''Verifies user is authorized'''
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," " probably unauthorised user"

    def should_be_login_link(self):
        '''Verifies login link is present'''
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    
    
class solve_quiz_and_get_code():
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
