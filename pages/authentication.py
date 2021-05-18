import locators.authentication as locators
from pages.base import Base


class AuthenticationPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, text ):
        self.write(locators.email_input, text)

    def create_account(self):
        self.click(locators.create_btn)