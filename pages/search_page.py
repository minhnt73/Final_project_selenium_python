from locators.search import SearchLocator
from pages.base import Base
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
        self.wait(10)

    def display_hints(self):
        self.wait(10)
        result = self.find_by_xpaths(SearchLocator.product_hints)
        list = []
        for i in result:
            list.append(i.text)
        print(list)

class Result_Search(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def input_value_search_file(self, text):
        self.write(SearchLocator.search_txb, text)

    def display_hints(self):
        result = self.find_by_xpaths(SearchLocator.product_hints)
        list_ = []
        for i in result:
            list_.append(self.get_text(i))
        print(list_)

    def click_hint1(self):
        self.click(SearchLocator.hint_ele1)

    def click_search_item(self):
        self.click(SearchLocator.search_item)

    def display_result(self):
        display = self.get_text(SearchLocator.result_all_search)
        unittest.TestCase().assertEqual(display,
                                        "display all dress",
                                        "False")


# --------------------------bai tap 07------------------------------------

class NoResultPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def input_text_search(self, text):
        self.write(SearchLocator.search_txb, text)

    def click_search(self):
        self.click(SearchLocator.search_item)

    def result_failse(self):
        no_result = self.get_text(SearchLocator.no_result)
        unittest.TestCase().assertEqual(no_result, 'No results were found for your search "dressSS"', 'Failse')
