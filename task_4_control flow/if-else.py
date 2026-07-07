#1. Check whether a number is positive, negative, or zero.
print("1. Check whether a number is positive, negative, or zero.")
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 2. Check whether a number is even or odd.
print("2. Check whether a number is even or odd.")
number = 6

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Find the largest of two numbers.
print("3. Find the largest of two numbers.")
num1 =10 
num2 = 6

if num1 > num2:
    print("Largest:", num1)
else:
    print("Largest:", num2)

#5. Check whether a year is a leap year.
print("5. Check whether a year is a leap year.")
year=2045
if year%4==0:
    print("This is a leap year")
else:
    print("this is not a leap year")

"""
6.Take a student's marks and print the grade.
Example:
90+ → A
75–89 → B
60–74 → C
Below 60 → Fail
"""
print("6.Take a student's marks and print the grade.")
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# 7. Check whether a person is eligible to vote.
print("7. Check whether a person is eligible to vote.")
age = 22

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 8. Check whether a character is Uppercase, Lowercase, Digit, or Special Character.
print("8. Check whether a character is Uppercase, Lowercase, Digit, or Special Character.")
ch = "mahek"
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

# 9. Check whether a number is divisible by both 3 and 5.
print("9. Check whether a number is divisible by both 3 and 5.")
number =5643

if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

# 10. Check whether a person is eligible for a driving license
print("10. Check whether a person is eligible for a driving license")


if age >= 18:
    print("Eligible for Driving License")
else:
    print("Not Eligible")