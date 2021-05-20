from locators.locator_create_account import CreateAccountLct
from pages.base import Base
import unittest


class CreateAccountPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_value(self):
        self.click(CreateAccountLct.tittle_radio_mrs)
        self.click(CreateAccountLct.date_birth_list)
        self.click(CreateAccountLct.date_birth_value)
        self.click(CreateAccountLct.month_birth_list)
        self.click(CreateAccountLct.month_birth_value)
        self.click(CreateAccountLct.year_birth_list)
        self.click(CreateAccountLct.year_birth_value)
        self.click(CreateAccountLct.sign_up_newsletter_checkbox)
        self.click(CreateAccountLct.state_list)
        self.click(CreateAccountLct.state_value)
        self.click(CreateAccountLct.country_list)
        self.click(CreateAccountLct.country_value)

    def enter_value(self, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12,
                    text13):
        self.write(CreateAccountLct.first_name_inf_tbx, text1)
        self.write(CreateAccountLct.last_name_inf_tbx, text2)
        self.write(CreateAccountLct.pw_tbx, text3)
        self.write(CreateAccountLct.first_name_addr_tbx, text4)
        self.write(CreateAccountLct.last_name_addr_tbx, text5)
        self.write(CreateAccountLct.company_tbx, text6)
        self.write(CreateAccountLct.address_tbx, text7)
        self.write(CreateAccountLct.address2_tbx, text8)
        self.write(CreateAccountLct.city_txb, text9)
        self.write(CreateAccountLct.zip_code_tbx, text10)
        self.write(CreateAccountLct.add_inf_txt, text11)
        self.write(CreateAccountLct.home_phone_tbx, text12)
        self.write(CreateAccountLct.mobile_phone_tbx, text13)

    def click_button(self):
        self.click(CreateAccountLct.button_regiser)

    def result_mess(self):
        mess = self.get_text(CreateAccountLct.result_mess)
        unittest.TestCase().assertEqual(mess,
                                        "Welcome to your account. Here you can manage all of your personal information and orders.",
                                        "False")
