import locators.home_page as locators
from pages.base import Base


class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in(self):
        self.click(locators.sign_in_btn)

    # Bài tập 02


    #YOUR PERSONAL INFORMATION

    # def tittle_radio(self):
    #     ele = self.find_xpath(Locator.radio_Mrs_id)
    #     self.click_button(ele)
    #
    # def first_name_inf(self, value):
    #     ele = self.find_xpath(Locator.first_name_inf_textbox_id)
    #     self.send_data(ele, value)
    #
    # def last_name_inf(self, value):
    #     ele = self.find_xpath(Locator.last_name_inf_textbox_id)
    #     self.send_data(ele, value)
    #
    # def password_text(self, value):
    #     ele = self.find_xpath(Locator.password_txt_id)
    #     self.send_data(ele, value)
    #
    # def dateBirth(self):
    #     ele = self.find_xpath(Locator.date_birth_id)
    #     self.click_button(ele)
    #     ele1 = self.find_xpath(Locator.days_value_id)
    #     self.click_button(ele1)
    #
    #     ele2 = self.find_xpath(Locator.month_birth_id)
    #     self.click_button(ele2)
    #     ele3 = self.find_xpath(Locator.month_value_id)
    #     self.click_button(ele3)
    #
    #     ele4 = self.find_xpath(Locator.years_birth_id)
    #     self.click_button(ele4)
    #     ele5 = self.find_xpath(Locator.years_value_id)
    #     self.click_button(ele5)
    #
    # def sign_up_newsletters(self):
    #     ele = self.find_xpath(Locator.signup_newsletters_id)
    #     self.click_button(ele)
    #
    # #YOUR ADDRESS
    #
    #
    # def firstName_addr(self,value):
    #     ele = self.find_xpath(Locator.first_name_addr_id)
    #     self.send_data(ele,value)
    #
    # def lastName_addr(self,value):
    #     ele = self.find_xpath(Locator.last_name_addr_id)
    #     self.send_data(ele,value)
    #
    # def company(self,value):
    #     ele = self.find_xpath(Locator.company_textbox_id)
    #     self.send_data(ele,value)
    #
    # def address(self,value):
    #     ele = self.find_xpath(Locator.address_txt_id)
    #     self.send_data(ele,value)
    #
    # def city(self,value):
    #     ele = self.find_xpath(Locator.city_txt_id)
    #     self.send_data(ele,value)
    #
    # def state(self):
    #     ele = self.find_xpath(Locator.select_state_id)
    #     self.click_button(ele)
    #     ele1 = self.find_xpath(Locator.value_state_id)
    #     self.click_button(ele1)
    #
    # def zip_code(self,value):
    #     ele = self.find_xpath(Locator.zip_code_id)
    #     self.send_data(ele,value)
    #
    # def country(self):
    #     ele = self.find_xpath(Locator.country_txt_id)
    #     self.click_button(ele)
    #     ele1 = self.find_xpath(Locator.value_country_id)
    #     self.click_button(ele1)
    #
    # def add_inf(self,value):
    #     ele = self.find_xpath(Locator.additional_inf_id)
    #     self.send_data(ele,value)
    #
    # def homePhone(self,value):
    #     ele = self.find_xpath(Locator.home_phone_id)
    #     self.send_data(ele,value)
    #
    # def mobilePhone(self,value):
    #     ele = self.find_xpath(Locator.mobile_phone_id)
    #     self.send_data(ele,value)
    #
    # #def address_alias(self):
    #     #ele = self.find_locator(Lacator.address_alias_id)
    #     #self.clear_data(ele)
    #     #ele1 = self.find_locator(Lacator.address_alias_id)
    #     #self.send_data(ele1)
    #
    # def register_btn(self):
    #     ele = self.find_xpath(Locator.button_registration_id)
    #     self.click_button(ele)
