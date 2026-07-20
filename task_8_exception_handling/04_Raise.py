# 1.Accept age from the user. Raise an exception if the age is negative.
try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age==0:
         raise ValueError("Age cannot be Zero.")

    print("Age:", age)

except ValueError as e:
    print(e)

# 2.Marks should be between 0 and 100.
try:
    marks=int(input("Enter marks : "))
    if 0 < marks > 100:
        raise ValueError("Enter valid marks")
    print("marks : ",marks)
except ValueError as e:
    print(e) 

# 3.Password must have at least 8 characters.
try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    print("Password accepted.")

except ValueError as e:
    print(e)

# 4.Raise an error if the withdrawal amount is greater than the balance. 
try:
    balance=60000
    amount=int(input("Enter amount : "))
    if amount>balance:
        raise ValueError("Insufficient Balance.")
    else:
        print("transition completed!!!")
except ValueError as e:
    print(e)

# 5.Accept a number. Raise an exception if it is odd.
try: 
    number=int(input("Enter number : "))
    if number % 2!=0:
        raise ValueError("Enter even number")
    else:
        print("Number : ",number)

except ValueError as e:
    print(e)

# Raise an exception if age is below 18.

try:
    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("Not eligible to vote.")

    print("Eligible")

except ValueError as e:
    print(e)