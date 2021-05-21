from locators.contact_us import ContactUs
from pages.base import Base


class ContactPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_contact_us_btn(self):
        self.click(ContactUs.contact_us_btn)

    def select_value(self):
        self.click(ContactUs.subject_select)
        self.click(ContactUs.subject_value)

    def enter_value(self, text1,text2,text3):
        self.write(ContactUs.email_txb, text1)
        self.write(ContactUs.order_txb, text2)
        self.write(ContactUs.message_txb,text3)

    def select_file(self, text):
        self.write(ContactUs.attach_file_select, text)

    def click_send(self):
        self.click(ContactUs.send_btn)
