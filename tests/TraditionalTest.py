import time

import allure

from Pages.BasePage import BasePage
from Pages.TraditionalPage import TraditionalLaptop


class DarazMobileAppTest(BasePage):

    @allure.step("Traditional laptop Search")
    def test_traditional_laptop(self):
        app = TraditionalLaptop(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.traditional()
        app.done_btn()

