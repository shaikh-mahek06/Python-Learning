#1. Arithmetic Operators
#1. Write a program to add two numbers

a=10
b=20
add=a+b
print("addition is :",add)

#2.Write a program to find the area of a rectangle.
l=5
b=7
area=l*b
print("Area of rectangle is :", area)

# 3.Take two numbers and print: Sum, Difference, Product, Division

num1=15
num2=5

print("num1 is:",num1)
print("num2 is :",num2)

sum=num1+num2
print("sum is :",sum)

Difference=num1-num2
print("Difference is :",Difference)

Product=num1*num2
print("Product is : ", Product)

Division=num1/ num2
print("Division is : ",Division)

# 4. Write a program to find the remainder when one number is divided by another.

m=100
n=7

remainder=m%n
print("remainder is :",remainder)

# 5. Write a program to find the square and cube of a number using operators.

number=9
print("number :",number)
square=number**2
print("square is :",square)
cube=number**3
print("cube is : ",cube)
 
#6.Write a program to calculate the average of three numbers.
x=10
y=20
z=30

average=(x+y+z)/3
print("average is :",average)


# 2 2. Comparison  Operators
print("Comparison  Operators")

number1=50
number2=35

print("number1 :",number1)
print("number2 :",number2)

#1.Check whether two numbers are equal.
print("1.Check whether two numbers are equal.")

print(number1==number2)

# 2.Find the greater number between two numbers.
print("2.Find the greater number between two numbers.")

if number1>number2:
    print("number1 is greater:",number1)
else:
    print("number2 is greater:",number2)

# 3.Check whether a person is eligible to vote 
print("3.Check whether a person is eligible to vote")
age=20
print("age :",age)

if age >= 18:
    print("You can vote")
else:
    print("You can't vote")


# 3. Assignment Operators
print("3. Assignment Operators")

# 1 Increase a variable by 10 using +=.
print("Increase a variable by 10 using +=.")

var=50
print("var is :", var)
var +=10
print("updated var  is :",var)

#2.Decrease a variable by 5 using -=.
print("Decrease a variable by 5 using -=.")
var -= 5
print("updated var  is :",var)

# 3.Double the value using *=.
print("Double the value using *=.")

var*=2
print("updated var  is :",var)

# 4.Find floor division using //=.
print("4.Find floor division using //=.")
var //=3
print("updated var  is :",var)

#4. Logical Operators
print("4. Logical Operators")

#1.Check whether a person can vote (age ≥ 18 and citizenship is Indian).
print("age is ",age)
citizenship = "Indian"
print('citizenship = "Indian"')
if age >=18 and citizenship == "Indian":
    print("you can vote") 
else:
    print("you cant vote")

#2.Check whether a student passed both subjects.
hindi=int(input("enter your hindi marks : "))
marathi=int(input("enter your marathi marks : "))

if hindi>=36 and marathi >=36:
    print("you are passed")

elif hindi>=36 and marathi<=36:
    print("you are failed in marathi")
elif hindi<=36 and marathi>=36:
    print("you are failed in hindi ")
else:
    print("you failed in both")

# 3.Check whether a number is divisible by both 3 and 5.
print(" 3.Check whether a number is divisible by both 3 and 5.")
print("number is :",number1)


if number1%3==0 and number1%5==0 :
    print("it is divisible by both")
else:
    print("it is not divisible by both")

#4.Check whether a number is divisible by 3 or 5
print("4.Check whether a number is divisible by 3 or 5")

print("number is :",number1)


if number1%3==0  :
    print("it is divisible by 3")
elif number1%5==0:
     print("it is not divisible by 5")
else:
    print("it is not divisible by none")

#5.Check whether a user can log in
print("5.Check whether a user can log in")

username="Mahek"
password="Mahek2005"

user=input("enter your username : ")
pas=input("enter your password : ")

if username==user and password==pas:
    print("you can login")
elif username!=user and password==pas:
    print("your username is wrong")
elif username==user and password!=pas:
    print("your password is wrong")
else:
    print("you can't login")

# 6.Check whether a person gets a discount: Age > 60 or Student
print("age : ",age)
is_student=True

if age >=60 or is_student==True:
    print("you got discount!!! ")
else:
    print(" you did'nt got discount :( ")

# 5.Identity Operators
print("5.Identity Operators")

#1.Compare two variables using is.
print("1.Compare two variables using is.")

o=44
print("o : ",o)
p=45
print("p : ",p)
print(o is p)

#2.Compare two lists using ==.
print("2.Compare two lists using ==. and is")
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
print(list1==list2)
print(list1 is list2)

#6. Membership Operators
print("6. Membership Operators")
#1.Check whether "Python" is present in a list.
print("1.Check whether Python is present in a list.")
ls=["Java","C++","Python","C#"]
print("ls : ",ls)
print("Python" in ls)

# 2.Check whether a character exists in a string
print("2.Check whether a character exists in a string")

word="python"
print('p' in word)

#3.Check whether a key exists in a dictionary.
print("3.Check whether a key exists in a dictionary.")

dic ={
    "name" :"mahek",
    "age":21,
    "city":"pune"
}
print("age " in dic)

#4.Use not in to check a missing item.
print("4.Use not in to check a missing item.")

print("css"not in ls)