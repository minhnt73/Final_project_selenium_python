import unittest
from selenium import webdriver
from pages.product_detail_page import ShareToTwitterPage
import chromedriver_autoinstaller
import time


class baitap12(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')

    def test_baitap12(self):
        TC = ShareToTwitterPage(self.driver)
        TC.ClickDetailProduct()
        TC.ShareTwitter()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
