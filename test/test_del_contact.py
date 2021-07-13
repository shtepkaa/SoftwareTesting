from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    check_empty_filling(app)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


def check_empty_filling(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))