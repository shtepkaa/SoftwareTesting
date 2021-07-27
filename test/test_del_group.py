import random

from model.group import Group
import random


# def test_delete_some_group(app):
def test_delete_some_group(app, db):
    check_empty_filling(app, db)

    # old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()

    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    # index = randrange(len(old_groups))
    # app.group.delete_group_by_index(index)

    # assert len(old_groups)-1 == len(new_groups)
    assert len(old_groups) - 1 == app.group.count()

    # new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()

    # old_groups[index:index+1] = []
    old_groups.remove(group)
    assert old_groups == new_groups


def check_empty_filling(app, db):
    # if app.group.count() == 0:
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
