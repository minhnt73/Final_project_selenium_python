class Base:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, time):
        return self.driver.implicitly_wait(time)

    def find_by_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def write(self, locator, text):
        return self.driver.find_xpath(locator).send_keys(text)

    def click(self, locator):
        return self.find_xpath(locator).click()

    def clear(self, locator):
        return self.find_xpath(locator).clear()

