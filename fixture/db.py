import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
        # autocommit=True чтобы данные не кэшировались

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, "
                           "email, email2, email3 from addressbook")
            "where deprecated = '0000-00-00 00:00:00' ставить бесполезно, сейчас запись в БД тоже удаляется"
            for row in cursor:
                (id, firstname, lastname, address, homephone, mobile, workphone, secondaryphone,
                 email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                    homephone=homephone, mobile=mobile, workphone=workphone,
                                    secondaryphone=secondaryphone, address=address,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()


