from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="changed", middlename="changed",
                                   lastname="changed", nickname="changed", title="changed",
                                   company="changed", address="changed",
                                   homenumber="987987987", mobilenumber="876876876",
                                   worknumber="765765765", fax="654654654", email="someaddress@test.com",
                                   email2="someaddress2@test.com", email3="someaddress3@test.com",
                                   homepage="www.something.com", bday="11", bmonth="February", byear="2001", aday="7",
                                   amonth="June", ayear="2023", address2="changed2", phone2="543543543",
                                   notes="changed"))
    app.session.logout()
