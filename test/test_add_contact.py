# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(firstname="Qwerty", middlename="Qwe", lastname="Asda",
                            nickname="Lotr", title="Agent", company="Deep Space Core Mining",
                            address="Elm Street", homenumber="123123123", mobilenumber="234234234",
                            worknumber="345345345", fax="456456456", email="qwerty.asda@gmail.com",
                            email2="qwerty.asda+2@gmail.com", email3="qwerty.asda+3@gmail.com",
                            homepage="google.com", bday="19", bmonth="December", byear="1977",
                            aday="24", amonth="November", ayear="2005", address2="Hamburger Hill",
                            phone2="567567567", notes="Lorem ipsum"))
    app.session.logout()
