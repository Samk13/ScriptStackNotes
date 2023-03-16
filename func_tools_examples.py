from functools import singledispatch

@singledispatch
def add(a, b):
    """The generic function"""
    raise NotImplementedError('Unsupported type')

@add.register(int)
def _(a, b):
    print(f"Arguments types are: {type(a), type(b)}")
    print(a + b)

@add.register(str)
def _(a, b):
    print(f"Arguments types are: {type(a), type(b)}")
    print(a + b)

@add.register(tuple)
def _(a, b):
    print(f"Arguments types are: {type(a), type(b)}")
    print(a + b)

if __name__ == "__main__":
    add(1, 3)
    add("a", "b")
    add((1,), (2,))
