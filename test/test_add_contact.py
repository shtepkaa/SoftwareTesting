# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from model.contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.setup_new_contact(driver, Contact(firstname="figu", middlename="fhug", lastname="ihfuge", mobile="74575"))
        self.submit_contact_creation(driver)
        self.return_home_page(driver)
        self.logout(driver)

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/index.php")

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def setup_new_contact(self, driver, contact):
        # add new contact
        driver.find_element_by_link_text("add new").click()
        # filling information about new contact
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile)

    def submit_contact_creation(self, driver):
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_home_page(self, driver):
        driver.find_element_by_link_text("home page").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
