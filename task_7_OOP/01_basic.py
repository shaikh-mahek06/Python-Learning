# 1. Student Class

# Create a Student class with:

# constructor
# name
# age
# roll_no
# display() method

# Create 3 objects and print their details. 
print("# 1. Student Class")

class student():
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no

    def display(self):
        print("Name:",self.name,"Age:",self.age, "Roll_No:",self.roll_no)

s1=student("mahek",21,34)
s2=student("sara",23,35)
s3=student("dino",26,36)
s1.display()
s2.display()
s3.display()

# 2. Employee Class
# Create an Employee class with emp_id ,name ,salary
print("# 2. Employee Class")

class employee():
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
e1=employee(165,"emma",50000)
print(e1.salary,e1.name)

# 3. Car Class
# Create a Car class having brand model year
# Create two car objects and print details using a method.
print("# 3. Car Class")

class car():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def show(self):
        print("brand : ",self.brand)
        print("model : ",self.model)
        print("year : ",self.year)

c1 = car("Toyota", "Fortuner", 2023)
c2 = car("Honda", "City", 2022)
print(c1.show())
print(c2.show())

# 4. Book Class
# Store : title,author,price
# Create multiple books and display details.
print("# 4. Book Class")

class book():
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def details(self):
        print(self.title,self.author,self.price)

b1=book("Peer-e-kamil","umama ahemad",486)
b2=book("The art of letting go","Nick",542)
print(b1.details())
print(b2.details())

# 8. Rectangle Class

# Constructor accepts : length ,breadth

# Methods: area(),perimeter()
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print(r.area())
print(r.perimeter())