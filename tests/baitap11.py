import unittest
from selenium import webdriver
from pages.product_detail_page import ProductDetailPage
import chromedriver_autoinstaller
import time


class baitap11(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_baitap11(self):
        TC = ProductDetailPage(self.driver)
        TC.ViewProduct()
        time.sleep(5)
        TC.CheckDisplay()
        TC.CheckQuantity('0','1')
        TC.CheckProduct()


        print('test bai tap 11 completed...')


if __name__ == '__main__':
    unittest.main()
