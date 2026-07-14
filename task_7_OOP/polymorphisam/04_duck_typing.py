class duck():
    def sound(self):
        print("quack quack")

class dog():
    def sound(self):
        print("brak brak")

def make_sound(animal):
    animal.sound()

d1=dog()
d2=duck()
make_sound(d1)
make_sound(d2)

# Example 2 (Multiple Classes)
class bird():
    def fly(self):
        print("bird is flaying")

class plane():
    def fly(self):
        print("plane is flaying")

def start(object):
    object.fly()

o1=bird()
o2=plane()
start(o1)
start(o2)
# 3
class Bike:

    def start(self):
        print("Bike Started")

class Car:

    def start(self):
        print("Car Started")

def start_vehicle(vehicle):
    vehicle.start()

b = Bike()
c = Car()

start_vehicle(b)
start_vehicle(c)