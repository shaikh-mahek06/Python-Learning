# 1.Build a simple calculator using match-case.
num1=int(input("Enter the number 1 : "))
num2=int(input("Enter the number 2 : "))
print("Select operations")
print("1.Addition")
print("2.Substraction")
print("3.Multiplaction")
print("4.Division")
choice=int(input("Enter the choice : "))

match choice:
    case 1:
        add=num1+num2
        print("Addition is : ",add)
    case 2:
        sub=num1-num2
        print("Substraction is : ",sub)
    case 3:
        mul=num1*num2
        print("Multiplaction is : ",mul)
    case 4:
        if num2 !=0:
            div=num1/num2
            print("Division is : ",div)
        else:
            print("can't divide by 0")
    case _:
        print("Invalid choice")

#2.Input a day number (1–7) and print the day name using match-case.
print("2.Input a day number (1–7) and print the day name using match-case.")
choice =int(input("Enter a days number(1-7) : "))

match choice:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Enter valid choice code")

"""Build a simple ATM menu using match-case.
1.	Balance
2. Deposit
3. Withdraw
4. Exit
"""
print("3.Build a simple ATM menu using match-case.")

print("1.Balance")
print("2.Deposit")
print("3.Withdraw")
print("4.Exit")

Balance=int(input("Enter Balance :"))

choice=int(input("Enter choice : "))

match choice:
    case 1:
        print("Total Balance : ",Balance)
        
    case 2:
        Deposit=int(input("Enter Deposit : "))
        new_bal=Balance+Deposit
        print("Total Balance : ",new_bal)
    case 3:
        Withdraw=int(input("Enter Withdraw : "))
        if Balance >= Withdraw:
            c=Balance-Withdraw
            print("Total Balance : ",c)
        else:
            print("Insufficient Balance")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice")

        


