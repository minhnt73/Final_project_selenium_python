import unittest
from selenium import webdriver
from pages.buy_page import baitap9Page
import chromedriver_autoinstaller
import time


class baitap09(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_baitap09(self):
        TC = baitap9Page(self.driver)
        TC.select_products()
        TC.change_amount_prod()
        TC.check_price()
        TC.check_out('minh@gmail.com', 'Minh123')


if __name__ == '__main__':
    unittest.main()
