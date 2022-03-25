import time

import allure

from Pages.BasePage import BasePage
from Pages.ListViewPage import ListView


class DarazMobileAppTest(BasePage):

    @allure.step("Changing The Product View")
    def test_listView_laptop(self):
        app = ListView(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.list_view()

