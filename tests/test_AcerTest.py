import time

import allure

from Pages.BasePage import BasePage
from Pages.AcerPage import AcerLaptop


class OpenAppTest(BasePage):
    @allure.step("Acer laptop Search")
    def test_acer_laptop(self):
        app = AcerLaptop(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.acer_laptop()
        app.done_btn()

