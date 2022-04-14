from model.group import Group
from model.contact import Contact


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contacts_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(),
                       middlename=contact.middlename.strip(),
                       lastname=contact.lastname.strip(), nickname=contact.nickname.strip(),
                       title=contact.title.strip(), company=contact.company.strip(),
                       address=contact.address.strip(), homenumber=contact.homenumber.strip(),
                       mobilenumber=contact.mobilenumber.strip(), worknumber=contact.worknumber.strip(),
                       fax=contact.fax.strip(), email=contact.email.strip(), email2=contact.email2.strip(),
                       email3=contact.email3.strip(), homepage=contact.homepage.strip(),
                       address2=contact.address2.strip(), notes=contact.notes.strip(), bday=contact.bday,
                       bmonth=contact.bmonth, byear=contact.byear, aday=contact.aday, amonth=contact.amonth,
                       ayear=contact.ayear, phone2=contact.phone2)
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
