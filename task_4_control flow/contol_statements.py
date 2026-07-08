# 1 Print numbers from 1 to 100.
# Stop immediately when the number becomes 57.

print("1.Print numbers from 1 to 100. Stop immediately when the number becomes 57.")

for i in range(1,101):
    if i==57:
        break
    
    print(i)

"""2.Print numbers from 1 to 30.
Skip numbers divisible by both 3 and 5.
"""

print("2.Print numbers from 1 to 30. Skip numbers divisible by both 3 and 5.")

for i in range(1,31):
    if i%3==0 and i%5==0:
        continue
    else:
        print(i)
"""Write a menu-driven program:
1. Add
2. Subtract
3. Exit
The program should keep running until the user selects Exit.
(Use a while loop and break.)
"""

while True:
    num1=int(input("enter numer 1:"))
    num2=int(input("enter numer 2:"))
    print("enter 1 for Addition")
    print("enter 2 for Substraction")
    print("enter 3 for Exit")
    choice=int (input("Enter the choice :"))
    
    if choice==1:
        add=num1+num2
        print("Addition is : ",add)
    elif choice==2:
        sub=num1-num2
        print("Substraction is : ",sub)
    elif choice==3:
        break

"""3.Ask the user to enter a password.
The program should keep asking until the correct password is entered.
Use a while loop.
"""
password="pata_nahi"
while True:
    pas=input("Enter your password : ")
    if password==pas:
        print("Login completed.....")
        break
    else:
        print("Wrong password try again") 
    
#4 Guess the number game.
print("Guess the number game between 1-100")

number=38
while True:
    num=int(input("Enter your number : "))
    if number==num:
        print("you won the game!!!!!")
        break
    else:
        print("Better Luck next time")

        