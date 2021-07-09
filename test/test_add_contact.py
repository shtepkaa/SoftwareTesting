from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="figu", middlename="fhug", lastname="ihfuge", mobile="74575"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)


