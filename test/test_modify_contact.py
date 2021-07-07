from model.contact import Contact
import time

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="1", middlename="1", lastname="1", mobile="1"))
    app.session.logout()


def test_modify_firstname_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="firstname new"))
    app.session.logout()


def test_modify_middlename_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="middlename new"))
    app.session.logout()


def test_modify_lastname_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="lastname new"))
    app.session.logout()


def test_modify_mobile_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mobile="mobile new"))
    app.session.logout()
