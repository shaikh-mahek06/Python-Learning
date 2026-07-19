# 1. Create a Student class with a private variable __name. Print it using a method.
class student():
    def __init__(self):
        self.__name="mahek"

    def display(self):
        print(self.__name)

s=student()
s.display()

# Question 2 : Create an Employee class with a private variable __salary. Display it using a method.
class employee():
    def __init__(self,salary):
        self.__salary=salary
    def display(self):
        print(self.__salary)
e=employee(70000)
e.display()


# Question 3 : Create a BankAccount class with a private variable __balance. Try accessing it directly from outside the class.
class BankAccount():
    def __init__(self,balance):
        self.__balance=balance

c=BankAccount(3000)
# print(c.__balance)

# Question 4 : Create a Student class with a private method __display(). Call it through a public method.
class student():
    def __display(self):
        print("privet method")
    def public(self):
        print(self.__display())

s1=student()
s1.public()
        
# Question 5 : Create a Person class with a private variable __age. Access it using name mangling.

class Person:

    def __init__(self):
        self.__age = 21

p = Person()

print(p._Person__age)