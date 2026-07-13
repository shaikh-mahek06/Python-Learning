# Question 1 
# Create:

# Animal
#    ↓
# Mammal
#    ↓
# Dog

# Methods:

# eat()
# walk()
# bark()

# Call all three methods
class animal():
    def eat(self):
        print("some animals eats other animals")
class mammal(animal):
    def walk(self):
        print("all mammals have ability of walking")
class dog(mammal):
    def bark(self):
        print("dog can bark")

d1=dog()
d1.eat()
d1.walk()
d1.bark()

# Question 2 
# Create:
# GrandFather
#       ↓
# Father
#       ↓
# Son
# Methods:
# land()
# house()
# bike()
# Call all methods.

class grandfather():
    def land(self):
        print("grandfather owns a land")

class father(grandfather):
    def house(self):
        print("father owns a house")

class son(father):
    def bike(self):
        print("son owns a bike")

s1=son()
s1.land()
s1.house()
s1.bike()

# Question 3 

# Create:

# BankAccount
#       ↓
# SavingsAccount
#       ↓
# PremiumSavings

# Add:

# account_details()
# interest_rate()
# premium_benefits()

# Call all three methods using the PremiumSavings object.

class bank_acc():
    def acc_details(self):
        print("account number can be anything")

class saving_acc(bank_acc):
    def intrest_rate(self ):
        print("the rate of intrest is 7")

class premium_saving(saving_acc):
    def premium_benefits(self):
        print("this is premium  benefits")

p1=premium_saving()
p1.acc_details()
p1.intrest_rate()
p1.premium_benefits()

