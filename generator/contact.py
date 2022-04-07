import random
import string
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
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
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    phone_numbers = string.digits
    return prefix + "".join([random.choice(phone_numbers) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


testdata = [Contact(firstname=random_string("firstname: ", 8),
                    middlename=random_string("middlename: ", 8),
                    lastname=random_string("lastname: ", 12),
                    nickname=random_string("nickname: ", 8),
                    title=random_string("title: ", 6),
                    company=random_string("company: ", 18),
                    address=random_string("address: ", 10),
                    homenumber=random_phone("homenumber: ", 12),
                    mobilenumber=random_phone("mobilenumber: ", 12),
                    worknumber=random_phone("worknumber: ", 12),
                    phone2=random_phone("phone2: ", 12),
                    fax=random_phone("fax: ", 12),
                    email=random_string("email: ", 16),
                    email2=random_string("email2: ", 16),
                    email3=random_string("email3: ", 16),
                    homepage=random_string("homepage: ", 20),
                    bday=str(random.randint(1, 29)),
                    bmonth=random.choice(months),
                    byear=str(random.randint(1940, 1980)),
                    aday=str(random.randint(1, 29)),
                    amonth=random.choice(months),
                    ayear=str(random.randint(1981, 2021)),
                    address2=random_string("address2: ", 16),
                    notes=random_string("notes: ", 50))
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    with open(file, "w") as out:
        jsonpickle.set_encoder_options("json", indent=4)
        out.write(jsonpickle.encode(testdata))
