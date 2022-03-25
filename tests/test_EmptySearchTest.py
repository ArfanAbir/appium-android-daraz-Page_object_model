import time

import allure

from Pages.BasePage import BasePage
from Pages.EmptySearchPage import EmptySearch


class DarazMobileAppTest(BasePage):
    @allure.step("Testing as Empty Search")
    def test_empty_search(self):
        app = EmptySearch(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar(" ")
        app.click_search_btn()

