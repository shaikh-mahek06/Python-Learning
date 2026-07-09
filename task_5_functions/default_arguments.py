# 1.Create a function with one default argument. 
print("# 1.Create a function with one default argument.")
def fun(text=":)"):
    print(text)

fun()

# 2.Create a function with two default arguments. 
print('2.Create a function with two default arguments.' )
def add(a=0,b=0):
    print(a+b)

add()

# 3.Override the default values.
print("# 3.Override the default values.")
def greet(name="xyz") :
    print(name)
greet("mahek")

# 4.Calculate interest using default rate. 
print("4.Calculate interest using default rate. ")
def intrest(principal,year,rate=10):
    calc_int=(principal*year*rate)/100
    print(calc_int)

intrest(2000,3)

# 5.Print employee details using default department. 
print("5.Print employee details using default department. ")
def employee(name, salary, department="HR"):
    print("Name:", name)
    print("Salary:", salary)
    print("Department:", department)

employee("Mahek", 50000)