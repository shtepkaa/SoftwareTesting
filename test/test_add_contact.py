from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="figu", middlename="fhug", lastname="ihfuge", mobile="74575", homephone="65476", workphone="576", secondaryphone="33",
                      address='jediafhc', email='odfej', email2='frdj', email3='jdfr')
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
