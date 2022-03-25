import time

import allure

from Pages.BasePage import BasePage
from Pages.EnglishToBanglaPage import EnglishToBangla


class OpenAppTest(BasePage):

    @allure.step("Changing Apps Language")
    def test_change_language(self):
        app = EnglishToBangla(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.account_icon()
        app.language_icon_click()
        app.language()
        app.bangla_language()
        app.apply_btn()

