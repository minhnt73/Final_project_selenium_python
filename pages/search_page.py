from locators.search import SearchLocator
from pages.base import Base


class SearchPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_value_search(self, text):
        self.write(SearchLocator.search_txb, text)

    def clear_value_search(self):
        self.clear(SearchLocator.search_txb)
