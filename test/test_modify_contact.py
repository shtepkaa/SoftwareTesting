from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="1", middlename="1", lastname="1", mobile="1"))
    app.session.logout()