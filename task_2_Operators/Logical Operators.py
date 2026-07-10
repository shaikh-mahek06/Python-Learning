
#4. Logical Operators
print("4. Logical Operators")

#1.Check whether a person can vote (age ≥ 18 and citizenship is Indian).
age=20
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