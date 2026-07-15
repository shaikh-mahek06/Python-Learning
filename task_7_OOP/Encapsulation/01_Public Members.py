# Question 1 :Create  a Student class with a public variable name and print it
class student():
    def __init__(self,name):
        self.name=name

    def print_name(self):
        print(self.name)
    

s1=student("mahek")
s1.print_name() 

# Question 2 :Create an Employee class with public variables emp_id and salary. Display them.
class employee():
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary

    def display(self):
        print(self.emp_id)
        print(self.salary)
e1=employee(165,50000)
e1.display()

# Question 3 : Create a Car class with a public method start().
class car():
    def start(self):
        print("car is starting...")

c1=car()
c1.start()

# Question 4 : Create a Book class with public variables title and author. Print them.
class book():
    def __init__(self,author,title):
        self.author=author
        self.title=title

    def display(self):
        print("Author : ",self.author)
        print("Title : ",self.title)

b1=book("Umera ahemad","peer e kamil")
b1.display()
    
# Question 5 : Create a BankAccount class with a public variable balance. Modify it from outside the class.

class BankAccount():
    def __init__(self):
        self.balance=10000

b=BankAccount()
print("before : ",b.balance)
b.balance=5000
print("after : ",b.balance)


    