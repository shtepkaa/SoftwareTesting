from model.contact import Contact


def check_exist(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))


def test_modify_first_contact(app):
    check_exist(app)
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="1", middlename="1", lastname="1", mobile="1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_firstname_first_contact(app):
    check_exist(app)
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="firstname new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_middlename_first_contact(app):
    check_exist(app)
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="middlename new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_lastname_first_contact(app):
    check_exist(app)
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="lastname new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_mobile_first_contact(app):
    check_exist(app)
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(mobile="mobile new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)