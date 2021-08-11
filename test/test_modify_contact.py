from model.contact import Contact
import random


def check_empty_filling(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test"))


def test_modify_some_contact(app, db, check_ui):
    check_empty_filling(app, db)
    a = app.contact.get_contact_list()
    b = db.get_contact_list()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    modif_contact = Contact(firstname="new", middlename="test", lastname="test")
    app.contact.modify_contact_by_id(contact.id, modif_contact)
    new_contacts = db.get_contact_list()

    # have to set these parameters before assert
    old_contacts[index] = modif_contact
    old_contacts[index].id = new_contacts[index].id

    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)