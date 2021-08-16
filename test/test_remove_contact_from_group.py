from model.contact import Contact
from model.group import Group
import random
# from fixture.orm import ORMFixture

# orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def check_empty_filling(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))


def test_delete_contact_from_group(app, db, orm):
    # global orm
    check_empty_filling(app, db)
    groups = db.get_group_list()
    group = random.choice(groups)
    app.contact.check_number_contacts_in_group(db, group)
    contacts_in_group_before_delete = orm.get_contacts_in_group(group)
    app.contact.remove_contact_from_group_by_id(group, orm, db)
    contacts_in_group_after_delete = orm.get_contacts_in_group(group)
    assert len(contacts_in_group_before_delete) - 1 == len(contacts_in_group_after_delete)
