import time
import unittest
from selenium import webdriver
from pages.buy_page import BuyPage
import chromedriver_autoinstaller


class BuyProduct(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_BuyPage(self):
        TC = BuyPage(self.driver)
        TC.select_products()
        TC.compare_price()
        TC.checkout_product_step01()
        TC.confirm_user()
        TC.checkout_product_final()



if __name__ == '__main__':
    unittest.main()
