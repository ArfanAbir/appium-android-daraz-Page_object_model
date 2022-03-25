import time

import allure

from Pages.BasePage import BasePage
from Pages.AsusPage import AsusLaptop


class DarazMobileAppTest(BasePage):

    @allure.step("Asus laptop Search")
    def test_asus_laptop(self):
        app = AsusLaptop(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.asus_laptop()
        app.done_btn()

