import time
import unittest
from selenium import webdriver
from pages.buy_page import baitap8Page
import chromedriver_autoinstaller


class baitap8(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_BuyPage(self):
        TC = baitap8Page(self.driver)
        TC.select_products()
        TC.compare_price()
        TC.checkout_product_step01()
        TC.confirm_user('minh@gmail.com','Minh123')
        TC.checkout_product_final()
        TC.message_display()



if __name__ == '__main__':
    unittest.main()
