# Question 1: Age Validation
class AgeError(Exception):
    pass
try:
    age=int(input("enter age : "))
    
    if age<0:
        raise AgeError("Age cant be negative  ")
    
    print("age : ",age)
except AgeError as e:
    print(e)

# Question 2: Bank Balance
class InsufficientBalanceError(Exception):
    pass

try:
    balance = 5000
    amount = int(input("Enter amount: "))

    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance.")

    print("Transaction Successful")

except InsufficientBalanceError as e:
    print(e)

# Question 3: Invalid Marks
class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    print("Marks:", marks)

except InvalidMarksError as e:
    print(e)


# Question 4: Invalid Password
class PasswordError(Exception):
    pass

try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise PasswordError("Password is too short.")

    print("Password Accepted")

except PasswordError as e:
    print(e)

# Question 5: Invalid Salary
class SalaryError(Exception):
    pass

try:
    salary = int(input("Enter salary: "))

    if salary < 0:
        raise SalaryError("Salary cannot be negative.")

    print("Salary:", salary)

except SalaryError as e:
    print(e)