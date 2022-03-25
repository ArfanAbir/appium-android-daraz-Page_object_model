import time

from Pages.HomePage import HomePage
from Locators.Locators import LoginLocators


class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator = LoginLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_first_next_button(self):
        self.find_element(*self.locator.first_next_buton_id).click()

    def change_language(self):
        time.sleep(4)
        self.find_element(*self.locator.allow_button_id).click()

    def skip_button_click(self):
        time.sleep(4)
        self.find_element(*self.locator.skip_button).click()
