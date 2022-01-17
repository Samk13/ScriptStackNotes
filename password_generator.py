import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits

char_pool = ''.join([upper, lower, digits])


def generate_password(length=10):
    print(''.join(random.choices(char_pool, k=length)))

n = input("How long you want your PS? ")
# the loop is to give options to choose the right one:

for i in range(10):
     generate_password(int(n))
