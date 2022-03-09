from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="new", middlename="new", lastname="new", nickname="new", title="new",
                                company="new", address="new", homenumber="000987987", mobilenumber="000876876",
                                worknumber="000765765", fax="000654654", email="somenewaddress@test.com",
                                email2="somenewaddress2@test.com", email3="somenewaddress3@test.com",
                                homepage="www.somethingnew.com", bday="13", bmonth="October", byear="1955",
                                aday="14", amonth="July", ayear="2002", address2="new2", phone2="000543543",
                                notes="new"))
    app.contact.edit_first(Contact(firstname="changed", middlename="changed",
                                   lastname="changed", nickname="changed", title="changed",
                                   company="changed", address="changed",
                                   homenumber="987987987", mobilenumber="876876876",
                                   worknumber="765765765", fax="654654654", email="someaddress@test.com",
                                   email2="someaddress2@test.com", email3="someaddress3@test.com",
                                   homepage="www.something.com", bday="11", bmonth="February", byear="2001", aday="7",
                                   amonth="June", ayear="2023", address2="changed2", phone2="543543543",
                                   notes="changed"))
