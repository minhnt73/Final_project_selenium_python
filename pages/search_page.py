from locators.search import SearchLocator
from pages.base import Base
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class SearchPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_value_search(self, text):
        self.write(SearchLocator.search_txb, text)

    def clear_value_search(self):
        self.clear(SearchLocator.search_txb)


class SearchHintProduct(Base):
    def __init__(self, driver):
        super(SearchHintProduct, self).__init__(driver)

    def input_value_search_file(self, text):
        self.write(SearchLocator.search_txb, text)

    def display_hints(self):
        result = self.find_by_xpaths(SearchLocator.product_hints)
        list_ = []
        for i in result:
            list_.append(self.get_text(i))
        print(list_)

class Result_Search(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def input_value_search_file(self, text):
        self.write(SearchLocator.search_txb, text)

    def display_result(self):
        result = self.find_by_xpaths(SearchLocator.result_search)
        self.










