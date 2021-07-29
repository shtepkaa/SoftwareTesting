from model.contact import Contact
from model.group import Group
import random
import time
from fixture.orm import ORMFixture


def check_empty_filling(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))


def test_add_contact_to_group(app, db):
    check_empty_filling(app, db)
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    random_group_number = random.randint(1, len(db.get_group_list()))
    app.contact.add_contact_to_group_by_id(contact.id, random_group_number)
    # Проверка, что записей в группе стало +1 через БД


def test_delete_contact_from_group(app, db):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    check_empty_filling(app, db)

    groups = db.get_group_list()
    group = random.choice(groups)

    contacts_before_delete = app.contact.count_contacts_by_group_id(group_id=group.id, orm=orm)

    while contacts_before_delete == 0:
        group = random.choice(groups)
        contacts_before_delete = app.contact.count_contacts_by_group_id(group_id=group.id, orm=orm)

    app.contact.delete_contact_from_group_by_id(group_id=group.id, orm=orm)
    contacts_after_delete = app.contact.count_contacts_by_group_id(group_id=group.id, orm=orm)
    assert contacts_before_delete - 1 == contacts_after_delete
