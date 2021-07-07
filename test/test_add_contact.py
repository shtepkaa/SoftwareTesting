from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="figu", middlename="fhug", lastname="ihfuge", mobile="74575"))
    #app.return_home_page()

