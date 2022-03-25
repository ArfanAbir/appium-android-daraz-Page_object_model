import time

import allure

from Pages.BasePage import BasePage
from Pages.DarazMallSearchPage import DarazMall


class DarazMobileAppTest(BasePage):
    @allure.step("Daraz mall Search")
    def test_darazmall_search(self):
        app = DarazMall(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.darazmall_icon()

