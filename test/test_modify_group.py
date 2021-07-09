from model.group import Group


def check_exist(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))


def test_modify_first_group(app):
    check_exist(app)
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="1", header="1", footer="1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_name_first_group(app):
    check_exist(app)
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="new name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_header_first_group(app):
    check_exist(app)
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="new header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_footer_first_group(app):
    check_exist(app)
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="new footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)