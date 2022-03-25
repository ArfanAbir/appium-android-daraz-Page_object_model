import time

from Pages.HomePage import HomePage
from Locators.Locators import LoginLocators


class EnglishToBangla(HomePage):

    def __init__(self, driver):
        self.locator = LoginLocators
        self.driver = driver
        super(EnglishToBangla, self).__init__(driver)

    def click_first_next_button(self):
        self.find_element(*self.locator.first_next_buton_id).click()

    def change_language(self):
        time.sleep(4)
        self.find_element(*self.locator.allow_button_id).click()

    def skip_button_click(self):
        time.sleep(4)
        self.find_element(*self.locator.skip_button).click()

    def account_icon(self):
        time.sleep(3)
        self.find_element(*self.locator.account_icon).click()

    def language_icon_click(self):
        time.sleep(3)
        self.find_element(*self.locator.language_icon).click()

    def language(self):
        time.sleep(3)
        self.find_element(*self.locator.language).click()

    def bangla_language(self):
        time.sleep(3)
        self.find_element(*self.locator.bangla_language).click()

    def apply_btn(self):
        time.sleep(3)
        self.find_element(*self.locator.apply_btn).click()
