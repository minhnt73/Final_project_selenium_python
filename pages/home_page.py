from locators.locator_home_page import HomePageLct
from pages.base import Base


class HomePage(Base):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def click_sigin_btn(self):
        self.click(HomePageLct.sign_in_btn)


