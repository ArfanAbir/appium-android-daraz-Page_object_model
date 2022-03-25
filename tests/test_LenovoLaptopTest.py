import time

import allure

from Pages.BasePage import BasePage
from Pages.LenovoLaptopPage import LenovoLaptop


class DarazMobileAppTest(BasePage):
    @allure.step("Lenovo laptop Search")
    def test_lenovo_laptop(self):
        app = LenovoLaptop(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.lenovo_laptop()
        app.done_btn()

