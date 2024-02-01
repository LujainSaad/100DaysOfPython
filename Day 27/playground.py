# *args: unlimited arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(1, 3, 6))


# **kwargs: many keywords arguments
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")  # kw["make"] will crash if there is no arguments
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
