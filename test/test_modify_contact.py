from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="1", middlename="1", lastname="1", mobile="1"))


def test_modify_firstname_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="firstname new"))


def test_modify_middlename_first_contact(app):
    app.contact.modify_first_contact(Contact(middlename="middlename new"))


def test_modify_lastname_first_contact(app):
    app.contact.modify_first_contact(Contact(lastname="lastname new"))


def test_modify_mobile_first_contact(app):
    app.contact.modify_first_contact(Contact(mobile="mobile new"))
