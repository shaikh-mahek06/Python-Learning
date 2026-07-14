from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound (self):
        pass


class dog(animal):
    def sound(self):
        print("bark bark")

d1=dog()
d1.sound()

# Example 2: Multiple Child Classes
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class square(shape):
    def area(self):
        print("Area=side*side")

class rectangle(shape):
    def area(self):
        print("area=2*length*breadth")
s=square()
s.area()
r=rectangle()
r.area()
# Example 3: Abstract Class with a Normal Method
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle Stopped")

class Car(Vehicle):

    def start(self):
        print("Car Started")

c = Car()

c.start()
c.stop()

# 4. Create an abstract class Payment with a pay() method. Implement it in UPI.

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):

    def pay(self):
        print("Payment Successful using UPI")

u = UPI()
u.pay()