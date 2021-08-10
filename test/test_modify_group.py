from model.group import Group
import random


def check_empty_filling(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))


def test_modify_some_group(app, db, check_ui):
    check_empty_filling(app, db)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    modif_group = Group(name="new", header="new", footer="new")
    app.group.modify_group_by_id(group.id, modif_group)
    new_groups = db.get_group_list()

    # have to set these parameters before assert
    old_groups[index] = modif_group
    old_groups[index].id = new_groups[index].id

    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
