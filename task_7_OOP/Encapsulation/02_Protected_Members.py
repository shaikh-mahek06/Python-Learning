# Question 1 : Create a Student class with a protected variable _name. Print it using a method.
class student():
    def __init__(self):
        self._name="mahek"
s1=student()
print(s1._name)

# Question 2:Create an Employee class with a protected variable _salary. Access it in a child class.
class employee():
    def __init__(self,salary):
        self._salary=salary

class manager(employee):
    def display(self):
        print(self._salary)

m1=manager(5000)
m1.display()

# Question 3 : Create a Person class with a protected method _greet(). Call it from a child class.
class person():
    def __init__(self):
        pass
    def _greet(self):
        print("Have a nice day!!!!")
class human(person):
    def display(self):
        print(self._greet())

h=human()
h.display()

#Question 4 :Create a Vehicle class with a protected variable _speed. Print it in a child class Car.

class Vehicle:

    def __init__(self, speed):
        self._speed = speed

class Car(Vehicle):

    def display(self):
        print("Speed:", self._speed)

c = Car(120)
c.display()

# Question 5 : Create a BankAccount class with a protected variable _balance. Display it using a method in the same class.

class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def show_balance(self):
        print("Balance:", self._balance)

account = BankAccount(10000)
account.show_balance()