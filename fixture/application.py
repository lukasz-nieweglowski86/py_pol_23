from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.ui import Select
import json
import os.path


class Application:
    target = {}

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def return_json_data(self):
        json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        with open(json_file) as f:
            target = json.load(f)
            return target

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith(self.return_json_data()["baseUrl"]) and
                len(wd.find_elements_by_name("searchstring")) > 0):
            wd.get(self.base_url)

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
