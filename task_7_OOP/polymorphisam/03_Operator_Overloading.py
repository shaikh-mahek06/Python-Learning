class calculator():
    def __init__(self,num):
        self.num=num

    def __add__(self, other):
        print(self.num + other.num)

    def __sub__(self, other):
        print(self.num - other.num)

    def __mul__(self, other):
        print(self.num * other.num)

    def __eq__(self, other):
        print(self.num == other.num)
        

    
        

s1=calculator(70)
s2=calculator(90)
s1+s2
s1-s2
s1*s2
s1==s2

# 2.Create a class Student that adds the marks of two students using the + operator.


class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(75)
s2 = Student(85)

print("Total Marks =", s1 + s2)
