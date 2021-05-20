from locators.locator_sign_in import SignInLct
from pages.base import Base
import unittest


class SignInPage(Base):
    def __init__(self, driver):
        super(SignInPage, self).__init__(driver)

    # def enter_email_addr(self, text):
    #     self.write(SignInLct.email_txb, text)

    def enter_email_addr(self, value):
        self.write(SignInLct.email_txb, value)

    def click_create_btn(self):
        self.click(SignInLct.create_btn)

    def display_result(self):
        display = self.get_text(SignInLct.display_messg)
        unittest.TestCase().assertEqual(display, "An account using this email address has already been registered. Please enter a valid password or request a new one.", "errorMessage")


