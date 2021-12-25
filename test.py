from enum import Enum


class Colors(Enum):
    red = "red"
    blue = "blue"
    green = "green"


for c in Colors:
    print(c.value)


def test1(*args):
    for i in args:
        if i < 3:
            print(i, "> 3")


a = 'shortaeasdfasdgfsfdgasdfgasdfgasdfgshortaeasdfasdgfsfdgasdfgasdfgasdfgshortaeasdfasdgfsfdgasdfgasdfgasdfg'
b = 'shortaeasdfasdgfsfdgasdfgasdfgasdfgshortaeasdfasdgfsfdgasdfgasdfgasdfgshortaeasdfasdgfsfdgasdfgasdfgasdfg'
c = 521323231232323
d = 521323231232323
print(a is b)  # True
print(c is d)  # True
