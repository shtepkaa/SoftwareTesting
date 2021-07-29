"""import re
from random import randrange
"""
from model.contact import Contact

"""
def check_empty_filling(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="figu", lastname="ihfuge", mobile="74575", homephone="65476", workphone="576", secondaryphone="33",
                      address='jediafhc', email='odfej', email2='frdj', email3='jdfr'))
"""


def check_empty_filling_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="figu", lastname="ihfuge", mobile="74575", homephone="65476", workphone="576", secondaryphone="33",
                      address='jediafhc', email='odfej', email2='frdj', email3='jdfr'))


def test_compare_all_contact_info(app, db):
    check_empty_filling_db(app, db)
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)

"""
def test_phones_on_home_page(app):
    check_empty_filling(app)
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
        contact_from_edit_page)


def test_emails_on_home_page(app):
    check_empty_filling(app)
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_firstname_on_home_page(app):
    check_empty_filling(app)
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname


def test_lastname_on_home_page(app):
    check_empty_filling(app)
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_address_on_home_page(app):
    check_empty_filling(app)
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address
"""

"""
def test_phones_on_contact_view_page(app):
    check_empty_filling(app)
    index = randrange(len(app.contact.get_contact_list()))
    # если нет элементов H, W и т.д выкидывает, в последующем нужно делать проверку
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
"""

"""
def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
"""