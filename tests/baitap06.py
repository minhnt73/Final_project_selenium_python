import unittest
from selenium import webdriver
from pages.search_page import SearchHintProduct
from pages.search_page import Result_Search
from pages.base import Base
import chromedriver_autoinstaller
import time


class TestSearchHint(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_input_search_hint(self):
        TC = SearchHintProduct(self.driver)
        TC.wait(10)
        # WebDriverWait(webdriver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//input[@id="search_query_top"]')))
        TC.input_value_search_file("Dress")
        time.sleep(5)
        TC.display_hints()
        time.sleep(5)

    def test_result_display(self):
        TC = Result_Search(self.driver)

        TC.input_value_search_file('Dress')

        TC.wait(10)

        TC.display_hints()

        time.sleep(10)

        TC.click_hint1()

        TC.click_search_item()

        TC.display_result()

    def test_tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
