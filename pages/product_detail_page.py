from selenium.webdriver import ActionChains

from locators.product_detail_loactor import ProductDetailLocator
from pages.base import Base
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators.locator_home_page import HomePageLct
from locators.buy_locator import BuyLocator


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

    # -----------------------------BAI TAP 12 ---------------------------------------------


class ShareToTwitterPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def ClickDetailProduct(self):
        self.click(ProductDetailLocator.product_img)
        self.wait(5)

    def ShareTwitter(self):
        self.click(ProductDetailLocator.share_twitter_btn)
        self.wait(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.write(ProductDetailLocator.id_twitter, "NTM731990")
        self.write(ProductDetailLocator.pw_twitter, "Truongminh1990")
        self.click(ProductDetailLocator.login_button)
        time.sleep(5)
        self.click(ProductDetailLocator.twitter_btn_page)

    # ---------------------------------- BAI TAP 13 --------------------------------


class WriteAComment(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, value1, value2):
        self.click(HomePageLct.sign_in_btn)
        self.write(BuyLocator.email_address, value1)
        self.write(BuyLocator.password_txtb, value2)
        self.click(BuyLocator.signin_btn)
        self.click(BuyLocator.icon_home)

    def SelectProduct(self):
        self.click(ProductDetailLocator.product)

    def WriteComment(self, text1, text2):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="open-comment-form"]'))).click()
        self.write(ProductDetailLocator.title_field, text1)
        self.write(ProductDetailLocator.comment, text2)
        time.sleep(3)
        self.click(ProductDetailLocator.send_button)

    def MessageSuccess(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div/p[1]')))
        mess = self.get_text(ProductDetailLocator.message_noti)
        unittest.TestCase().assertEqual(mess,
                                        'Your comment has been added and will be available once approved by a moderator',
                                        'Fail')


# -----------------------------------BAI TAP 14 -------------------------------------------------

class SenToFriend(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def select_prod(self):
        self.click(ProductDetailLocator.product)

    def send_mail(self, text1, text2):
        self.click(ProductDetailLocator.send_to_a_friend)
        self.write(ProductDetailLocator.name_of_your_friend, text1)
        self.write(ProductDetailLocator.email, text2)
        self.click(ProductDetailLocator.send)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//p[contains(text(),"Your e-mail has been sent successfully")]')))
        self.wait(10)
        message = self.get_text(ProductDetailLocator.mess_conf)
        unittest.TestCase().assertEqual(message, 'Your e-mail has been sent successfully', 'Fail')

    def check_email(self, text, text1):
        self.driver.execute_script('''window.open("https://mail.google.com/","_blank");''')
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.write(ProductDetailLocator.id_email, text)
        self.click(ProductDetailLocator.continue_button)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type = 'password']")))
        self.wait(10)
        self.write(ProductDetailLocator.pw_email, text)
        self.click(ProductDetailLocator.continue_button)


