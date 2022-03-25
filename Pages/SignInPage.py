import time

from Pages.HomePage import HomePage
from Locators.Locators import LoginLocators


class SignInDaraz(HomePage):

    def __init__(self, driver):
        self.locator = LoginLocators
        self.driver = driver
        super(SignInDaraz, self).__init__(driver)

    def click_first_next_button(self):
        self.find_element(*self.locator.first_next_buton_id).click()

    def change_language(self):
        time.sleep(5)
        self.find_element(*self.locator.allow_button_id).click()

    def skip_button_click(self):
        time.sleep(5)
        self.find_element(*self.locator.skip_button).click()

    def account_icon(self):
        time.sleep(5)
        self.find_element(*self.locator.account_icon).click()

    def login_icon(self):
        time.sleep(5)
        self.find_element(*self.locator.login_signin).click()

    def login_with_password(self):
        time.sleep(5)
        self.find_element(*self.locator.login_with_password).click()

    def enter_phone_mobile(self,number):
        time.sleep(5)
        self.find_element(*self.locator.mobile_email).send_keys(number)

    def enter_password(self, password):
        time.sleep(5)
        self.find_element(*self.locator.password).send_keys(password)

    def click_login(self):
        time.sleep(2)
        self.find_element(*self.locator.login_btn).click()
