# import json
import jsonpickle
import random
import string
import os.path
from model.contact import Contact
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ " "*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname="", middlename="", lastname="", address="",
                    homephone="", workphone="", mobile="", secondaryphone="",
                    email="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), mobile=random_string("mobile", 10),
            homephone=random_string("home", 10), workphone=random_string("work", 10),
            secondaryphone=random_string("phone2", 10), address=random_string("address", 10),
            email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
