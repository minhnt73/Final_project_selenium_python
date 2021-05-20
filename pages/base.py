# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_by_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def click(self, locator):
        return self.find_by_xpath(locator).click()

    def write(self, locator, text):
        return self.find_by_xpath(locator).send_keys(text)

    def wait(self, time):
        return self.driver.implicitly_wait(time)

    def clear(self, locator):
        return self.find_by_xpath(locator).clear()

    def get_text(self,locator):
        return self.find_by_xpath(locator).text

