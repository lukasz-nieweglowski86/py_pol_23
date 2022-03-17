from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_form(self, group):
        self.app.set_value("group_name", group.name)
        self.app.set_value("group_header", group.header)
        self.app.set_value("group_footer", group.footer)

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
        self.group_cache = None

    def edit_first_group(self):
        self.edit_group_by_index(0)

    def edit_group_by_index(self, index, new_group_data):
        self.open_groups_page()
        self.select_group_by_index(index)
        self.enter_group_details_page()
        self.fill_form(new_group_data)
        self.submit_group_edition()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        self.open_groups_page()
        self.select_group_by_index(index)
        self.submit_group_deletion()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
