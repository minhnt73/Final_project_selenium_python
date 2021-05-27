import unittest
from selenium import webdriver
# import chromedriver_autoinstaller
from pages.newsletter_page import NewsLetterPage


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

class FinalProject(unittest.TestCase):
    def setUp(self) -> None:
        # chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')
        # WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')))

    def test_submit_newsletter(self):
        TC = NewsLetterPage(self.driver)
        TC.wait(10)
        TC.enter_email('tuuyiiy@gmail.com')
        TC.click_submit()
        TC.display_mess()

        print('Test baitap03 is completed...')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
