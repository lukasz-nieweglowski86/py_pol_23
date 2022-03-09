class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_form(self, group):
        self.app.change_value("group_name", group.name)
        self.app.change_value("group_header", group.header)
        self.app.change_value("group_footer", group.footer)

    def initiate_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def enter_group_details_page(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def submit_group_edition(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def submit_group_deletion(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        self.open_groups_page()
        self.initiate_group_creation()
        self.fill_form(group)
        self.submit_group_creation()
        self.return_to_groups_page()

    def edit_first_group(self, new_group_data):
        self.open_groups_page()
        self.select_first_group()
        self.enter_group_details_page()
        self.fill_form(new_group_data)
        self.submit_group_edition()
        self.return_to_groups_page()

    def delete_first(self):
        self.open_groups_page()
        self.select_first_group()
        self.submit_group_deletion()
        self.return_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
