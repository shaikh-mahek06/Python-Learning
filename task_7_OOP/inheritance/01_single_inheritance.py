# Example 1: Basic Single Inheritance
print("# Example 1: Basic Single Inheritance")
class animal():
    def eat(self):

        print("animal eats a grass")

class cow(animal):
    pass
c1=cow()
c1.eat()


# 2.Create a Vehicle class with a method start().
# Create a Car class inheriting from Vehicle.
# Add a method drive() in Car.
# Call both methods using the Car object.
print("02")
class vehicle():
    def start(self):
        print("vehicle is starting!!!!")

class car(vehicle):
    def drive(self):
        print("he is driving a car")

c1=car()
c1.start()
c1.drive()

# 3. Person → Student 
# Create a Person class with : name , age
# using a constructor.
# Create a Student class inheriting from Person.
# Create a student object and display name and age.
print("3. Person → Student ")
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

class student(person):
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

s1=student("Mahek",21)
s1.display()

# 4. Employee → Manager 
# Create an Employee class with: emp_id ,emp_name 
# Create a Manager class inheriting from Employee.
# Add a method display().
# Print all employee details.

print("4. Employee → Manager ")
class employee():
    def __init__(self,emp_id,emp_name):
        self.emp_id=emp_id
        self.emp_name=emp_name

class manager(employee):
    def display(self):
        print("emp_id : " ,self.emp_id)
        print("emp_name : " ,self.emp_name)

m1=manager(143,"emma")
m1.display()

# 5. BankAccount → SavingsAccount ⭐⭐
# Create a BankAccount class with:
# •	account_number 
# •	balance 
# Create a SavingsAccount class inheriting from it.
# Add a method to display balance

class bank_acc():
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance

class saving_acc(bank_acc):
    def display(self):
        print("Account no : ",self.acc_no)
        print("Balance : ",self.balance)
a1=saving_acc(3405,50000)
a1.display()

# 6. Book → EBook ⭐⭐
# Create a Book class with:
# •	title 
# •	author 
# Create an EBook class inheriting from Book.
# Add:
# •	file_size 
# Display all details.

class book():
    def __init__(self,title,author):
        self.title=title
        self.author=author
class Ebook(book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size=file_size
    def display(self):
        print("Title : ",self.title)
        print("Author : ",self.author)
        print("File_size : ",self.file_size)
b1=Ebook("Peer-e-kamil","umera ahemad", "128kb")
b1.display()

# 7. Teacher → MathTeacher ⭐⭐
# Create a Teacher class with a method:
# teach()
# Create a MathTeacher class inheriting from Teacher.
# Add:
# solve_problem()
# Call both methods.

class teacher():
    def teach(self):
        print("teaches a english")
class maths_teacher(teacher):
    def solve_problem(self):
        print("solves problem")

t1=maths_teacher()
t1.teach()
t1.solve_problem()

# 8. Shape → Circle ⭐⭐
# Create a Shape class with:
# draw()
# Create a Circle class inheriting from Shape.
# Add:
# area()
import math
class shape():
    def draw(self):
        print("draw a shape")

class circle(shape):
    def area(self,radius):
        print(math.pi*radius**2)

c1=circle()
c1.draw()
c1.area(3)

