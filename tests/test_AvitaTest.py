import time

import allure

from Pages.BasePage import BasePage
from Pages.AvitaPage import AvitaLaptop


class DarazMobileAppTest(BasePage):
    @allure.step("Avita laptop Search")
    def test_avita_laptop(self):
        app = AvitaLaptop(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.avita_laptop()
        app.done_btn()

