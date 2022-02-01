from functools import wraps

condition = True
test = ("Its true", "it's false")[not condition]
print(test)


def decorator_func(func_child):
    def wraper_func():
        print("start")
        func_child()
        print("end")

    return wraper_func


@decorator_func
def test():
    print("should be wrapped here")


test()


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        print("*args", args)
        print("**kwargs", kwargs)
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x, **kwargs):
    for i in kwargs:
        if i == "test":
            return "yesyyesyesy"
    print(kwargs)
    """Do some math."""
    return x + x


result = addition_func(4, test="SAmmmaskmas")
print(result)
