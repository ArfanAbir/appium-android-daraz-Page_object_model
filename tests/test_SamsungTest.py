import time

import allure

from Pages.BasePage import BasePage
from Pages.SamsungSearchpage import SamsungSearch


class DarazMobileAppTest(BasePage):

    @allure.step("Samsung laptop Search")
    def test_samsung_laptop(self):
        app = SamsungSearch(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("samsung")
        app.click_search_btn()

