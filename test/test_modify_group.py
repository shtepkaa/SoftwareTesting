from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="1", header="1", footer="1"))
    app.session.logout()


def test_modify_name_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="new name"))
    app.session.logout()


def test_modify_header_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="new header"))
    app.session.logout()


def test_modify_footer_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="new footer"))
    app.session.logout()