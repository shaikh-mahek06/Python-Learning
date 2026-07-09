#  1.Create a function that prints "Hello World".
def hello():
    print("Hello World")

hello()

# 2.Create a function to print your name.
def greet(name):
    print("hello",name)

greet("mahek shaikh")

# 3.Create a function to add two numbers.
def add(a,b):
    print("Addition is : ",a+b)

add(4533,5433)

# 4.Create a function to subtract two numbers.
def sub(a,b):
    print("Substaction is : ",a-b)

sub(4533,5433)

# 5.Create a function to multiply two numbers.
def multiply(a,b):
    print("Multiplaction is is : ",a*b)

multiply(4533,54)

# 6.Create a function to divide two numbers.
def division(a,b):
    print("Division is : ",a/b)

division(54332,43)

# 7.Create a function that prints the square of a number.
def square(a):
    print(f"square of {a} is : {a*a}")

square(5)

# 8.Create a function that prints whether a number is even or odd.
def even_odd(number):
    if number % 2 ==0:
        print(f"{number} is Even number")
    else:
        print(f"{number} is Odd number")

even_odd(6533)

# 9.Create a function that accepts three numbers and prints the largest.
def largest(a,b,c):
    larg_num=max(a,b,c)
    print("largest num is : ",larg_num)

largest(653,44,64)

# 10.Create a function that accepts a string and prints it in uppercase.

def uppercase(string):
    print(string.upper())

uppercase("life is full of blunders!!!")

# 11.Create a function that accepts a list and prints all elements.
print("Elements of list : ")
def elements(lst):
    for i in lst:
        print(i)

elements(["apple","banana","mango","watermelon"])

# 12.Create a function that accepts a list and prints all elements.
print("Elements of tuple : ")
def tup_element(tup):
    for i in tup:
        print(i)

tup_element(("apple","banana","mango","watermelon"))

# 13.Create a function that counts vowels in a string.
def count_vowels(string):
    vowels=("aeiouAEIOU")
    count=0
    for ch in string:
        if ch in vowels:
            count+=1
    print("Total number of vowels are : ",count)

count_vowels("life is full of blunders!!!")





















    
