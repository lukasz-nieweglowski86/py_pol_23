from model.contact import Contact
from random import randrange


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="new", middlename="new", lastname="new", nickname="new", title="new",
                                company="new", address="new", homenumber="000987987", mobilenumber="000876876",
                                worknumber="000765765", fax="000654654", email="somenewaddress@test.com",
                                email2="somenewaddress2@test.com", email3="somenewaddress3@test.com",
                                homepage="www.somethingnew.com", bday="13", bmonth="October", byear="1955",
                                aday="14", amonth="July", ayear="2002", address2="new2", phone2="000543543",
                                notes="new"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts
