import unittest
from selenium import webdriver
from pages.product_detail_page import SenToFriend
import chromedriver_autoinstaller
from selenium.webdriver import ActionChains
import time


class baitap13(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_send_to_friend(self):
        TC = SenToFriend(self.driver)
        TC.select_prod()
        TC.send_mail('minh', 'minhnta.lqa@gmail.com')
        TC.check_email("minhnta.lqa@gmail.com","Truongminh1990")
        print("Test bai tap 14 completed....")


if __name__ == '__main__':
    unittest.main()
