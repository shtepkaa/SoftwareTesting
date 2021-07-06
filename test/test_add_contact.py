# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="figu", middlename="fhug", lastname="ihfuge", mobile="74575"))
    app.session.logout()

