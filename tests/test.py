import unittest
from selenium import webdriver
import chromedriver_autoinstaller
from pages import home_page as _home_page
from pages import authentication as _authentication_page
import time
from selenium.webdriver.support import expected_conditions as EC


class CreateAccount(unittest.TestCase):
    def setUp(self) -> None:
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/')

    def test_createAccountFail(self):
        home_page = _home_page(self.driver)
        home_page.wait(5)
        home_page.click_sign_in()
        authentication_page = _authentication_page(self.driver)
        authentication_page.enter_email('minh@gmail.com')
        authentication_page.wait(5)
        authentication_page.create_account()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
