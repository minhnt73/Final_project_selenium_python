import unittest
from pages.contact_us_page import ContactPage
from selenium import webdriver
import chromedriver_autoinstaller


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

class SubmitContactForm(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php?controller=contact')

    def test_submit_contact_form(self):
        # WebDriverWait(webdriver, 10).until(
        # EC.presence_of_element_located((By.XPATH, '//div[@id= "contact-link"]//a[@title = "Contact Us"]')))

        TC = ContactPage(self.driver)
        TC.wait(10)
        TC.click_contact_us_btn()
        TC.select_value()
        TC.enter_value('abc@gmail.com', 'mau do', 'abcdef')
        # TC.select_file()
        TC.click_send()

        print('Test completed submit contact....')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
