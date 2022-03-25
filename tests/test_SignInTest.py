import time

import allure

from Pages.BasePage import BasePage
from Pages.SignInPage import SignInDaraz


class SignInDarazApp(BasePage):

    @allure.step("Sign in into Daraz Mobile App")
    def test_signin_daraz_mobile_app(self):
        app = SignInDaraz(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.account_icon()
        app.login_icon()
        app.login_with_password()
        app.enter_phone_mobile("01713086265")
        app.enter_password("abc123")
        app.click_login()

