import unittest
from selenium import webdriver
from pages.product_detail_page import WriteAComment
import chromedriver_autoinstaller
from selenium.webdriver import ActionChains
import time


class baitap13(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')


    def test_write_comment(self):
        TC = WriteAComment(self.driver)
        TC.login('minh@gmail.com','Minh123')
        TC.SelectProduct()
        TC.WriteComment('minh', 'Product is very good')
        TC.MessageSuccess()
        print("Test bai tap 13 completed....")



if __name__ == '__main__':
    unittest.main()
