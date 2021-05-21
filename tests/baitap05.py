import unittest
from selenium import webdriver
from pages.search_page import SearchPage
# from pages.base import Base
import chromedriver_autoinstaller


class TestSearch(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')

    def test_enter_value(self):
        TC = SearchPage(self.driver)
        TC.enter_value_search('dress')
        # TC = Base(self.driver)
        TC.clear_value_search()
        TC.wait(10)

    def test_tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
