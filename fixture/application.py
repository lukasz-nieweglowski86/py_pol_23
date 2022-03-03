from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def change_value(self, field_name, value):
        wd = self.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def select_value(self, element_name, value):
        wd = self.wd
        wd.find_element_by_name(element_name).click()
        Select(wd.find_element_by_name(element_name)).select_by_visible_text(value)

    def destroy(self):
        self.wd.quit()
