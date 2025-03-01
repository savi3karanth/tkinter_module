def add(*args):
    print(args[2])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 4, 5, 6, 7))


def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiply=5)
print()
def cal(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
cal(3, add=5, multiply=2)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
print(my_car)
#suppose we we dint give model name we get the key error
#my_car = Car(make="Nissan") ie KeyError: 'model'
#to fix that we just need to write .get

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan") # since model is not given
print(my_car.make)
print(my_car.model) #prints none without crashing bcz of .get method
print(my_car.color)
print(my_car.seats)

