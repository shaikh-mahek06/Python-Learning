# Question 1 ⭐

# Create:

# Person
#    ↓
# Student

# Parent constructor:name
# Child constructor:  roll
# Use super().

# Display both.

class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    
s1=student("mahek",21)
print(s1.name)
print(s1.roll)

# Question 2

# Create:

# Vehicle
#    ↓
# Car

# Vehicle constructor:brand
# Car constructor:model

class Vehicle():
    def __init__(self,brand):
        self.brand=brand
class car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
c1=car("xyz","abc")
print(c1.brand)
print(c1.model)

# Question 3 ⭐⭐⭐ (Most Important)

# Create:

# BankAccount
#       ↓
# SavingsAccount

# Parent constructor:

# account number
# balance

# Child constructor:

# interest rate

# Use super().

# Create an object and display all three values.

class bank_acc():
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
class saving_acc(bank_acc):
    def __init__(self,acc_no,balance,intrest):
        super().__init__(acc_no,balance)
        self.intrest=intrest

a1=saving_acc(4678,1000,10)
print(a1.acc_no)
print(a1.balance)
print(a1.intrest)

# example 4

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def show(self):
        super().eat()
        print("Dog is happy")
d1=Dog()
d1.eat()
d1.show()