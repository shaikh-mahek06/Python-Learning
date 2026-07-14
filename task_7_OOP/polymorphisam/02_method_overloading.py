# 1. Default Arguments

# Example

class Calculator:

    def add(self, a, b=0, c=0):
        print(a+b+c)


# 2. Using *args
c = Calculator()

c.add(10)
c.add(10,20)
c.add(10,20,30)

class calculator():
    def add(self,*args):
        print(sum(args))

c1=calculator()
c1.add(4,5,6,7,8,9)



# 3. Using **kwargs
class Student:

    def details(self, **info):
        for key, value in info.items():
            print(key, ":", value)

s = Student()

s.details(name="Mahek", age=21, city="Pune")


# 04
class Shape:

    def area(self, *args):
        if len(args) == 1:
            print("Square Area =", args[0] * args[0])
        elif len(args) == 2:
            print("Rectangle Area =", args[0] * args[1])
        else:
            print("Invalid Input")

s = Shape()

s.area(5)
s.area(4, 6)