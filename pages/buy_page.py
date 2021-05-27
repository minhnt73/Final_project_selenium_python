from locators.buy_locator import BuyLocator
from pages.base import Base
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class baitap8Page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def select_products(self):
        self.click(BuyLocator.product_no1)
        self.wait(10)
        self.click(BuyLocator.add_to_cart_btn)
        self.wait(10)
        self.click(BuyLocator.continue_shopping_btn)
        self.click(BuyLocator.icon_home)

        self.click(BuyLocator.product_no2)
        self.wait(10)
        self.click(BuyLocator.add_to_cart_btn)
        self.wait(10)
        self.click(BuyLocator.continue_shopping_btn)
        self.click(BuyLocator.icon_home)

        self.click(BuyLocator.product_no3)
        self.wait(10)
        self.click(BuyLocator.add_to_cart_btn)
        self.wait(10)
        self.click(BuyLocator.proceed_to_checkout_btn)

    def compare_price(self):
        time.sleep(10)
        ele = self.find_by_xpath(BuyLocator.product_1_price).text
        ele_ = ele.replace("$", "")

        ele1 = self.find_by_xpath(BuyLocator.product_2_price).text
        ele1_ = ele1.replace("$", "")
        ele2 = self.find_by_xpath(BuyLocator.product_3_price).text
        ele2_ = ele2.replace("$", "")
        totalProduct = self.find_by_xpath(BuyLocator.total_products).text
        totalProduct_ = totalProduct.replace("$", "")
        if float(ele_) + float(ele1_) + float(ele2_) == float(totalProduct_):
            print("True")
        else:
            print("False")
        self.wait(10)

    def checkout_product_step01(self):
        self.click(BuyLocator.proceed_to_checkout_summary_btn)
        self.wait(10)

    def confirm_user(self, text1, text2):
        self.write(BuyLocator.email_address, text1)
        self.wait(5)
        self.write(BuyLocator.password_txtb, text2)
        self.wait(10)
        self.click(BuyLocator.signin_btn)

    def checkout_product_final(self):
        self.click(BuyLocator.proceed_to_checkout_address_btn)
        self.wait(10)
        self.click(BuyLocator.agree_checkbox)
        self.wait(10)
        self.click(BuyLocator.proceed_to_checkout_shipping_btn)

        self.wait(10)
        self.click(BuyLocator.pay_by_bank)
        self.click(BuyLocator.i_confirm_my_oder)

    def message_display(self):

        display = self.get_text(BuyLocator.mess_confirm)
        unittest.TestCase().assertEqual(display,
                                        "Your order on My Store is complete.",
                                        "False")


# -------------------------------Bài tap 09---------------------------------------------
class baitap9Page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def select_products(self):
        self.wait(10)
        self.click(BuyLocator.product_1)
        self.wait(5)
        self.click(BuyLocator.add_to_cart)
        self.wait(5)
        self.click(BuyLocator.continue_shopping)
        self.click(BuyLocator.icon_home)
        self.wait(5)
        self.click(BuyLocator.product_2)
        self.wait(5)
        self.click(BuyLocator.add_to_cart)
        self.wait(5)
        self.click(BuyLocator.continue_shopping)
        self.wait(5)
        self.click(BuyLocator.icon_home)
        self.wait(5)
        self.click(BuyLocator.product_3)
        self.wait(5)
        self.click(BuyLocator.add_to_cart)
        self.wait(5)
        self.click(BuyLocator.continue_shopping)
        self.wait(5)
        self.click(BuyLocator.icon_home)
        self.wait(5)
        self.click(BuyLocator.product_4)
        self.wait(5)
        self.click(BuyLocator.add_to_cart)
        self.wait(5)
        self.click(BuyLocator.continue_shopping)
        self.wait(5)
        self.click(BuyLocator.icon_home)
        self.wait(5)
        # self.click(BuyLocator.product_5)
        # self.wait(5)
        # self.click(BuyLocator.add_to_cart)

    def change_amount_prod(self):
        self.click(BuyLocator.cart)
        self.wait(10)
        self.click(BuyLocator.add_icon)
        self.wait(5)
        self.click(BuyLocator.add_icon)
        self.wait(5)
        self.click(BuyLocator.add_icon)
        self.wait(5)
        self.click(BuyLocator.delete_icon)

    def check_price(self):

        # price_01 = self.get_text(BuyLocator.price_1)
        # price_01_ = price_01.replace("$", "")
        price_01 = self.get_text(BuyLocator.price_1)
        price_01_ = price_01.replace("$", "")
        print(price_01_)
        price_02 = self.get_text(BuyLocator.price_2)
        price_02_ = price_02.replace("$", "")
        print(price_02_)
        price_03 = self.get_text(BuyLocator.price_3)
        price_03_ = price_03.replace("$", "")
        print(price_03_)
        total_exp = self.get_text(BuyLocator.total_price_exp)
        total_exp_ = total_exp.replace("$", "")
        print(total_exp_)
        if float(price_02_) + float(price_03_) + float(price_01_) + 2.00 == float(total_exp_):
            print("True")
        else:
            print("Fail")

    def check_out(self, text1, text2):
        self.click(BuyLocator.proceed_checkout)
        self.wait(5)
        self.write(BuyLocator.email_address, text1)
        self.wait(5)
        self.write(BuyLocator.password_txtb, text2)
        self.click(BuyLocator.signin_btn)
        self.wait(5)
        self.click(BuyLocator.proceed_to_checkout_address_btn)
        self.wait(5)
        self.click(BuyLocator.proceed_checkout_shipping)
        mess = self.get_text(BuyLocator.popup_mess)
        unittest.TestCase().assertEqual(mess, "You must agree to the terms of service before continuing.", "Fail")
        self.wait(5)
        self.click(BuyLocator.popup_mess_close)
        self.wait(5)
        self.click(BuyLocator.agree_checkbox)
        self.wait(5)
        self.click(BuyLocator.proceed_checkout_shipping)
        self.wait(5)
        self.click(BuyLocator.pay_by_bank)
        self.wait(5)
        self.click(BuyLocator.i_confirm_my_oder)
        self.wait(5)
        message_confirm = self.get_text(BuyLocator.mess_confirm)
        unittest.TestCase().assertEqual(message_confirm, 'Your order on My Store is complete.', 'Fail')


# ---------------------------------BÀI TẬP 10-----------------------------------------------

class baitap10Page(Base):
    def __init__(self, driver):
        super(baitap10Page, self).__init__(driver)

    def select_product_20per(self):
        self.wait(10)
        element = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[7]/div/div[1]/div/a[1]/img')
        hov = ActionChains(self.driver).move_to_element(element)
        hov.perform()
        self.wait(10)
        self.click(BuyLocator.add_to_cart_sale20)
        self.wait(10)
        self.click(BuyLocator.proceed_check_btn)
        self.wait(5)

    def check_out(self, text1, text2):
        self.wait(5)
        self.click(BuyLocator.proceed_check_cart_btn)
        self.wait(5)
        self.write(BuyLocator.email_address, text1)
        self.write(BuyLocator.password_txtb, text2)
        self.click(BuyLocator.signin_btn)
        self.wait(5)
        self.click(BuyLocator.proceed_check_adress_btn)
        self.wait(5)
        self.click(BuyLocator.agree_checkbox)
        self.wait(5)
        self.click(BuyLocator.proceed_check_shipping_btn)
        self.wait(5)
        self.click(BuyLocator.pay_by_bank)
        self.wait(5)
        self.click(BuyLocator.i_confirm_my_oder)
        self.wait(5)
        mess = self.get_text(BuyLocator.message)
        unittest.TestCase().assertEqual(mess, 'Your order on My Store is complete.', 'Fail')
