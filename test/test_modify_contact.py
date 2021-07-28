from model.contact import Contact
import random


def check_empty_filling(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))


def test_modify_some_contact(app, db, check_ui):
    check_empty_filling(app, db)
    old_contacts = db.get_contact_list()
    index = random.randrange(len(old_contacts))
    contact = Contact(firstname="1", middlename="1", lastname="1", mobile="1")
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
