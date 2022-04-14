from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def initiate_adding_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_form(self, contact):
        # new contact form - name and first address
        self.app.set_value("firstname", contact.firstname)
        self.app.set_value("middlename", contact.middlename)
        self.app.set_value("lastname", contact.lastname)
        self.app.set_value("nickname", contact.nickname)
        self.app.set_value("title", contact.title)
        self.app.set_value("company", contact.company)
        self.app.set_value("address", contact.address)
        # new contact form - telephones
        self.app.set_value("home", contact.homenumber)
        self.app.set_value("mobile", contact.mobilenumber)
        self.app.set_value("work", contact.worknumber)
        self.app.set_value("fax", contact.fax)
        # new contact form - emails
        self.app.set_value("email", contact.email)
        self.app.set_value("email2", contact.email2)
        self.app.set_value("email3", contact.email3)
        self.app.set_value("homepage", contact.homepage)
        # new contact form - birthday and anniversary
        self.app.select_value("bday", contact.bday)
        self.app.select_value("bmonth", contact.bmonth)
        self.app.set_value("byear", contact.byear)
        self.app.select_value("aday", contact.aday)
        self.app.select_value("amonth", contact.amonth)
        self.app.set_value("ayear", contact.ayear)
        # new contact form - secondary address and phone number
        self.app.set_value("address2", contact.address2)
        self.app.set_value("phone2", contact.phone2)
        # new contact form - notes
        self.app.set_value("notes", contact.notes)

    def submit_adding_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def click_edit_icon_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def click_edit_icon_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def submit_contact_edition(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        self.click_edit_icon_by_index(0)

    def select_contact_by_index(self, index):
        self.click_edit_icon_by_index(index)

    def select_contact_by_id(self, id):
        self.click_edit_icon_by_id(id)

    def submit_contact_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def back_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith(self.app.return_json_data()["web"]["baseUrl"] + "/edit.php") and
                len(wd.find_elements_by_link_text("add next")) > 0):
            wd.find_element_by_link_text("home page").click()

    def add(self, contact):
        self.initiate_adding_new_contact()
        self.fill_form(contact)
        self.submit_adding_new_contact()
        self.back_to_home_page()
        self.contact_cache = None

    def edit_first(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_data):
        self.app.open_home_page()
        self.click_edit_icon_by_index(index)
        self.fill_form(new_data)
        self.submit_contact_edition()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_data):
        self.app.open_home_page()
        self.click_edit_icon_by_id(id)
        self.fill_form(new_data)
        self.submit_contact_edition()
        self.contact_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.submit_contact_deletion()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        self.app.open_home_page()
        self.select_contact_by_id(id)
        self.submit_contact_deletion()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                contact_firstname = element.find_element_by_xpath(".//td[3]").text
                contact_lastname = element.find_element_by_xpath(".//td[2]").text
                contact_address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=contact_firstname, lastname=contact_lastname, id=id,
                                                  address=contact_address, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, ))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homenumber = wd.find_element_by_name("home").get_attribute("value")
        mobilenumber = wd.find_element_by_name("mobile").get_attribute("value")
        worknumber = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homenumber=homenumber, mobilenumber=mobilenumber,
                       worknumber=worknumber, phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homenumber = re.search("H: (.*)", text).group(1)
        worknumber = re.search("W: (.*)", text).group(1)
        mobilenumber = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homenumber=homenumber, mobilenumber=mobilenumber, worknumber=worknumber, phone2=phone2)
