from locators.product_detail_loactor import ProductDetailLocator
from pages.base import Base
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductDetailPage(Base):
    def __init__(self, driver):
        super(ProductDetailPage, self).__init__(driver)

    def ViewProduct(self):
        self.click(ProductDetailLocator.product_img)
        self.wait(5)
        self.click(ProductDetailLocator.view_lager_icon)
        self.wait(5)

    def CheckDisplay(self):
        WebDriverWait(self.driver, 10).until(
            (EC.presence_of_element_located((By.XPATH, '//span[@class = "child"]'))))
        self.wait(5)
        productName = self.driver.find_element_by_xpath(ProductDetailLocator.product_name).text
        unittest.TestCase().assertEqual(productName, "Faded Short Sleeve T-shirts", "Fail")
        self.wait(5)
        # --------- Click vào button [Close] trên ảnh---------------------------------
        self.click(ProductDetailLocator.close_icon)
        self.wait(5)

    # --------------------Add to cart với Quantity =0 ----------------------------------
    def CheckQuantity(self, value1, value2):
        self.clear(ProductDetailLocator.quantity_field)
        self.wait(5)
        self.write(ProductDetailLocator.quantity_field, value1)
        self.wait(5)
        self.click(ProductDetailLocator.add_to_cart_button)
        self.wait(5)
        check_popup = self.get_text(ProductDetailLocator.popup_messg)
        unittest.TestCase().assertEqual(check_popup, 'Null quantity.', 'Fail')
        self.wait(5)
        self.click(ProductDetailLocator.popup_messg_close)
        self.wait(5)
        # ---------------------Add to cart với Quantity > 0 ------------------------------------
        self.clear(ProductDetailLocator.quantity_field)
        self.wait(5)
        self.write(ProductDetailLocator.quantity_field, value2)
        self.wait(5)
        self.click(ProductDetailLocator.add_to_cart_button)
        time.sleep(5)
        mess = self.driver.find_element_by_xpath(ProductDetailLocator.mess_confirm).text
        unittest.TestCase().assertEqual(mess, 'Product successfully added to your shopping cart', 'Fail')
        self.wait(5)
        self.click(ProductDetailLocator.close_icon_popup)
        self.wait(5)

    def CheckProduct(self):
        self.click(ProductDetailLocator.cart_btn)
        time.sleep(10)

        productInCart = self.get_text(ProductDetailLocator.product_in_cart)

        if productInCart != "":
            print("True")
        else:
            print("False")
