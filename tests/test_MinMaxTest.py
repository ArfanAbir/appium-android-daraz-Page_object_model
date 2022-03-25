import time

import allure

from Pages.BasePage import BasePage
from Pages.MinMaxPage import MinMaxPrice


class DarazMobileAppTest(BasePage):

    @allure.step("Set Minimum and Maximum Price")
    def test_min_max_price_laptop(self):
        app = MinMaxPrice(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.min_price("20000")
        app.max_price("90000")
        app.done_btn()

