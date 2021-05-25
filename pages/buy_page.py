from locators.buy_locator import BuyLocator
from pages.base import Base
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import unittest


class BuyPage(Base):
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

    def confirm_user(self):
        self.write(BuyLocator.email_address)
        self.wait(5)
        self.write(BuyLocator.password_txtb)
        self.wait(10)
        self.click(BuyLocator.signin_btn)

    def checkout_product_final(self):
        self.click(BuyLocator.proceed_to_checkout_summary_btn)
        self.wait(10)
        self.click(BuyLocator.proceed_to_checkout_summary_btn)
        self.wait(10)
        self.click(BuyLocator.agree_checkbox)
        self.wait(10)
        self.click(BuyLocator.pay_by_bank)
        self.click(BuyLocator.i_confirm_my_oder)

        display = self.get_text(BuyLocator.mess_confirm)
        unittest.TestCase().assertEqual(display,
                                        "Your order on My Store is complete.",
                                        "False")
