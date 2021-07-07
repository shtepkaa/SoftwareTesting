from model.group import Group


def check_exist(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))


def test_modify_first_group(app):
    check_exist(app)
    app.group.modify_first_group(Group(name="1", header="1", footer="1"))


def test_modify_name_first_group(app):
    check_exist(app)
    app.group.modify_first_group(Group(name="new name"))


def test_modify_header_first_group(app):
    check_exist(app)
    app.group.modify_first_group(Group(header="new header"))


def test_modify_footer_first_group(app):
    check_exist(app)
    app.group.modify_first_group(Group(footer="new footer"))