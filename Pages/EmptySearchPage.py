import time

from Pages.HomePage import HomePage
from Locators.Locators import LoginLocators


class EmptySearch(HomePage):

    def __init__(self, driver):
        self.locator = LoginLocators
        self.driver = driver
        super(EmptySearch, self).__init__(driver)

    def click_first_next_button(self):
        self.find_element(*self.locator.first_next_buton_id).click()

    def change_language(self):
        time.sleep(4)
        self.find_element(*self.locator.allow_button_id).click()

    def skip_button_click(self):
        time.sleep(4)
        self.find_element(*self.locator.skip_button).click()

    def search_bar_icon(self):
        time.sleep(4)
        self.find_element(*self.locator.search_bar).click()

    def search_input_bar(self, search):
        time.sleep(5)
        self.find_element(*self.locator.search_input).send_keys(search)

    def click_search_btn(self):
        time.sleep(4)
        self.find_element(*self.locator.search_btn).click()
