import time
import unittest
from selenium import webdriver
from pages.search_page import NoResultPage



class NoResultSearch(unittest.TestCase):
    def setUp(self):
        # chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_no_result_search(self):
        TC = NoResultPage(self.driver)
        TC.input_text_search('dressSS')
        time.sleep(10)
        TC.click_search()
        time.sleep(10)
        TC.result_failse()


if __name__ == '__main__':
    unittest.main()
