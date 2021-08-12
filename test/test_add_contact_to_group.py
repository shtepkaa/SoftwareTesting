from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def check_empty_filling(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))


def test_add_contact_to_group(app, db):
    global orm
    check_empty_filling(app, db)

    contacts = db.get_contact_list()
    contact = random.choice(contacts)

    groups = db.get_group_list()
    group = random.choice(groups)

    contacts_before_add = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    contacts_after_add = orm.get_contacts_in_group(group)

    assert len(contacts_before_add) + 1 == len(contacts_after_add)
