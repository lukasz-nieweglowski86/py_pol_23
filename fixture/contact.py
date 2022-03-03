

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def initiate_adding_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_form(self, contact):
        # new contact form - name and first address
        self.app.change_value("firstname", contact.firstname)
        self.app.change_value("middlename", contact.middlename)
        self.app.change_value("lastname", contact.lastname)
        self.app.change_value("nickname", contact.nickname)
        self.app.change_value("title", contact.title)
        self.app.change_value("company", contact.company)
        self.app.change_value("address", contact.address)
        # new contact form - telephones
        self.app.change_value("home", contact.homenumber)
        self.app.change_value("mobile", contact.mobilenumber)
        self.app.change_value("work", contact.worknumber)
        self.app.change_value("fax", contact.fax)
        # new contact form - emails
        self.app.change_value("email", contact.email)
        self.app.change_value("email2", contact.email2)
        self.app.change_value("email3", contact.email3)
        self.app.change_value("homepage", contact.homepage)
        # new contact form - birthday and anniversary
        self.app.select_value("bday", contact.bday)
        self.app.select_value("bmonth", contact.bmonth)
        self.app.change_value("byear", contact.byear)
        self.app.select_value("aday", contact.aday)
        self.app.select_value("amonth", contact.amonth)
        self.app.change_value("ayear", contact.ayear)
        # new contact form - secondary address and phone number
        self.app.change_value("address2", contact.address2)
        self.app.change_value("phone2", contact.phone2)
        # new contact form - notes
        self.app.change_value("notes", contact.notes)

    def submit_adding_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def click_edit_icon(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()

    def submit_contact_edition(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()

    def submit_contact_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def back_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def add(self, contact):
        self.initiate_adding_new_contact()
        self.fill_form(contact)
        self.submit_adding_new_contact()
        self.back_to_home_page()

    def edit_first(self, new_data):
        self.app.open_home_page()
        self.click_edit_icon()
        self.fill_form(new_data)
        self.submit_contact_edition()

    def delete_first(self):
        self.select_first_contact()
        self.submit_contact_deletion()
