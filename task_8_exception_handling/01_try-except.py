# 1 Write a program to divide two numbers. Handle the case when the denominator is zero.

try:
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))
    print(num1/num2)

except :
    if num2==0:
        print("Cannot divide by zero.")
    else:
        num1/num2

# Problem 2: Integer Input

# Ask the user to enter an integer.

# If the user enters a valid integer, print it.
# If the user enters text, handle the ValueError.

try:
    num =int(input("Enter number : "))
except ValueError:
    
    print("Enter valid number ")


# 3.Create a list of 5 elements. Ask the user for an index and print the value.
ls=[1,2,3,4,5]
try:
    index=int(input("Enter index : "))
    print("element : ", ls[index])
except IndexError:
    print("invalid index")

# 4.Access a key from a dictionary. 
dic={
    "name":"mahek",
    "age":21,
    "gender":"female",
    "blood_group":"B+"
}
try:
    print(dic["marks"])

except KeyError:
    print("invalid key")

# 5.Open a file named data.txt.
try:
    file=open("data.txt")
except FileNotFoundError:
    print("invalid filename")

# 6.Write a calculator that handles: Invalid input , Division by zero
try:
    n1=int(input("Enter the number 1 : "))
    n2=int(input("Enter the number 2 : "))
    
    print("Addition : ",n1+n2)
    print("Substraction : ",n1-n2)
    print("multiplaction: ",n1*n2)
    print("dividion : ",n1/n2)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("can't possible to divide number by zero")

#  7.Write a program that catches any unexpected exception.

try:
    num = int(input("Enter number: "))
    print(10 / num)

except Exception as e:
    print("Error:", e)