import time

import allure

from Pages.BasePage import BasePage
from Pages.GamingLaptopPage import GamingLaptop


class DarazMobileAppTest(BasePage):

    @allure.step("Searching for Gaming laptop")
    def test_gaming_laptop(self):
        app = GamingLaptop(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.category_arrow()
        app.gaming_laptop()
        app.done_btn()

