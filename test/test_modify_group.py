from model.group import Group
import random


def check_empty_filling(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))


def test_modify_some_group(app, db, check_ui):
    check_empty_filling(app, db)
    old_contacts = db.get_contact_list()
    index = random.randrange(len(old_contacts))
    group = Group(name="1", header="1", footer="1")
    app.group.modify_group_by_index(index, group)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Group.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                   key=Group.id_or_max)
