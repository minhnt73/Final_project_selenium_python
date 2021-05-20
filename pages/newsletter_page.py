from locators.newsletter import NewsLetter
from pages.base import Base
import unittest


class NewsLetterPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, value):
        self.write(NewsLetter.email_txb, value)

    def click_submit(self):
        self.click(NewsLetter.submit_btn)

    def display_mess(self):
        display = self.get_text(NewsLetter.result_mssg)
        unittest.TestCase().assertEqual(display,
                                        "Newsletter : You have successfully subscribed to this newsletter.",
                                        "False")
