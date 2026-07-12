# 9. Bank Account

# Create a BankAccount class.

# Instance variables

# account number
# holder name
# balance

# Methods

# deposit()
# withdraw()
# display_balance()

class bank():
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        total_bal=self.balance + amount
        print("Total balance : ",total_bal)
    def withdraw(self,amount):
        if amount<=self.balance:
            print("Total balance : ",self.balance - amount)
        else:
            print("low balance")
    def display_balance(self):
        print("Total balance : ",self.balance)


a1=bank(304,"emma",32000)
a1.deposit(3000)
a1.withdraw(5000)
a1.display_balance()

# 10. Circle Class

# Constructor takes radius.
# Methods
# area()
# circumference()
import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area of circle is : ", math.pi * self.radius**2)

    def circumference(self):
        print("circumference of circle is : ",2*math.pi*self.radius)
        
c1=circle(5)
c1.area()
c1.circumference()

# 11. Calculator Class

# Create methods: addition,subtraction, multiplication,division
class calculator():
    def __init__(self ,a,b):
        self.a=a
        self.b=b

    def addition(self):
        print("addition :",self.a+self.b)

    def subtraction(self):
        print("subtraction : ",self.a-self.b)

    def multiplication(self):
        print("multiplication : ",self.a*self.b)

    def division(self):
        print("division : ",self.a/self.b)

cl1=calculator(4566,7654)
cl1.addition()

# 12. Shopping Cart

# Store

# customer name
# total amount

# Methods

# add_item(price)
# remove_item(price)
# display_total()

class shopping_cart():
    def __init__(self,name,total):
        self.name=name
        self.total=total
    def add_item(self,price):
        print("Total amount : ",self.total+price)
    def remove_item(self,price):
        print("Total amount : ",self.total-price)
    def display_total(self):
        print("Total amount : ",self.total)

s1=shopping_cart("mahek",50000)
s1.add_item(5000)

# 13. Temperature Converter
class Temperature:
    def c_to_f(self, c):
        return (c * 9 / 5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5 / 9


t = Temperature()

print(t.c_to_f(25))
print(t.f_to_c(98.6))


# 14. Student Result
class StudentResult:
    def __init__(self, marks):
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        p = self.percentage()

        if p >= 90:
            return "A"
        elif p >= 75:
            return "B"
        elif p >= 50:
            return "C"
        else:
            return "Fail"


s = StudentResult([80, 90, 85, 75, 95])

print(s.total())
print(s.percentage())
print(s.grade())

# 15. Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18


p = Person("Mahek", 21)

print(p.is_adult())
