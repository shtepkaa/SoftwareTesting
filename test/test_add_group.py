from model.group import Group


def test_add_group(app):
    #old_groups = app.group.get_group_list()
    app.group.create(Group(name="rfdj", header="pfrohivwri", footer="GOEIPOTHE"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == new_groups


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
