from model.contact import Contact
import random


def test_delete_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="new", middlename="new", lastname="new", nickname="new", title="new",
                                company="new", address="new", homenumber="000987987", mobilenumber="000876876",
                                worknumber="000765765", fax="000654654", email="somenewaddress@test.com",
                                email2="somenewaddress2@test.com", email3="somenewaddress3@test.com",
                                homepage="www.somethingnew.com", bday="13", bmonth="October", byear="1955",
                                aday="14", amonth="July", ayear="2002", address2="new2", phone2="000543543",
                                notes="new"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                     key=Contact.id_or_max)
