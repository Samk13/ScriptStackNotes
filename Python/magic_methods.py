from inspect import getsource


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"This is a {self.color} car with {self.mileage} miles on it."

    def __add__(self, other):
        return self.mileage + other.mileage

    def __len__(self):
        return len(self.color)

    def __del__(self):
        pass
        # print("Car is destroyed")


bmw = Car("red", "100")


def test_car(car, *args, **kwargs):
    print(car)
    print(args)
    print(car.color)
    print(car.mileage)
    print(car + bmw)
    print(len(car))


print("===========")
print("car __name__", test_car.__name__)
print("funtion file name", test_car.__code__.co_filename)
print("funtion file conts", test_car.__code__.co_consts)
print("funtion arg count", test_car.__code__.co_argcount)
print("func first line no", test_car.__code__.co_firstlineno)
print("func co_flags", dir(test_car.__code__.__format__))
print(getsource(test_car))
print(getattr(test_car, "__name__"))
