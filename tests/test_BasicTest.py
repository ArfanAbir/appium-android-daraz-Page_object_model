import time

import allure

from Pages.BasePage import BasePage
from Pages.BasicComputerPage import BasicComputer


class DarazMobileAppTest(BasePage):

    @allure.step("Basic laptop Search")
    def test_basic_computer(self):
        app = BasicComputer(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.basic_computer()
        app.done_btn()

