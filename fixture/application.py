from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("localhost/addressbook/") and
                len(wd.find_elements_by_name("searchstring")) > 0):
            wd.get("http://localhost/addressbook/")

    def set_value(self, field_name, value):
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
