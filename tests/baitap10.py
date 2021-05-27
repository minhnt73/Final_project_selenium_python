import unittest
from selenium import webdriver
from pages.buy_page import baitap10Page
import chromedriver_autoinstaller
import time


class baitap10(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_baitap10(self):
        TC = baitap10Page(self.driver)
        TC.select_product_20per()
        TC.check_out('minh@gmail.com','Minh123')
        print("test bai tap 10 has been completed.....")


if __name__ == '__main__':
    unittest.main()
