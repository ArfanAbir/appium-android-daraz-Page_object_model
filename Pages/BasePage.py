import unittest

import allure
from appium import webdriver


class BasePage(unittest.TestCase):

    @allure.step("daraz-mobile")
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities=dict(platformName='Android', automationName='UiAutomator2', platformVersion='12',
                                      udid='emulator-5554',
                                      app="C:\\Users\\arfan\OneDrive\\Desktop\\project\\Python_Daraz_Appium_mobile\\APK\\daraz.apk")
        )
        print("Test Started.......")

    def tearDown(self):
        # self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
