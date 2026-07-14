# Question 1
# Animal
#    ↓
#   Dog

class animal():
    def sound(self):
        print("All animal makes sound")

class dog (animal):
    def sound(self):
        print("dogs bark -BHAU BHAU")
d1=dog()
d1.sound()

"""Question 2

Create:

Person
   ↓
Student"""

class person():
    def display(self):
        print("i am person")

class student(person):
    def display(self):
        print("i am student")

s1=student()
s1.display()

""" Question 3

Create:

Vehicle
   ↓
Car"""

class Vehicle():
    def start(self):
        print("Vehicle is starting.....")

class car(Vehicle):
    def start(self):
        print("car is starting...")

c1=car()
c1.start()

"""Question 4

Use super().

Animal
   ↓
Dog

Call the parent sound() first, then print "Dog Barks"."""


class animal():
    def sound(self):
        print("All animal makes sound")

class dog (animal):
    def sound(self):
        super().sound()
        print("dogs bark -BHAU BHAU")
d1=dog()
d1.sound()

"""Question 5

Create:

Employee
   ↓
Manager

Override:

work()

Call the parent method using super()."""

class employee():
    def work(self):
        print("work something")

class manager(employee):
    def work(self):
        super().work()
        print("they also works for something")

m1=manager()
m1.work()

"""Question 7 (Most Asked)

Create:

BankAccount
        ↓
SavingsAccount

Parent has:

display()

Child overrides display().

First show parent details using super().

Then show the interest rate."""

class bank_acc():
    def display(self):
        print("bank acc is activated")

class saving_acc(bank_acc):
    def __init__(self,intrest_rate):
        self.intrest_rate=intrest_rate
    def display(self):
        super().display()
        print(self.intrest_rate)

a1=saving_acc(8)
a1.display()
        