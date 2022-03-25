import time

import allure

from Pages.BasePage import BasePage
from Pages.MSILaptopPage import MSILaptop


class DarazMobileAppTest(BasePage):

    @allure.step("MSI laptop Search")
    def test_msi_laptop(self):
        app = MSILaptop(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.msi_laptop()
        app.done_btn()

