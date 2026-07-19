# 1.Write a program to divide two numbers. Display the result if possible. Print a message from the finally block.
print("1.Write a program to divide two numbers. Display the result if possible. Print a message from the finally block.")
try:
    num1=int(input("Enter the number : "))
    num2=int(input("Enter the number : "))
    div=print("Result : ",num1/num2)
except ZeroDivisionError:
    print("Can't possible ")

finally:
    print("end of code")

# 2.Open a file and display its contents. Ensure the file is closed using the finally block.
print("2.Open a file and display its contents. Ensure the file is closed using the finally block.")
try:
    file=open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("end of code")

# 3.Create a list and ask the user for an index. Handle invalid indexes and always print a completion message.
print("3.Create a list and ask the user for an index. Handle invalid indexes and always print a completion message.")
ls=[1,2,3,4,5]
try:
    index=int(input("Enter the index : "))
    print(ls[index])
except IndexError:
    print("Invalid index")
finally:
    print("end of code")

# 4.Access a student's marks from a dictionary. If the key doesn't exist, handle the exception and always display a closing message.
print("4.Access a student's marks from a dictionary. If the key doesn't exist, handle the exception and always display a closing message.")
dic={
    "name":"mahek",
    "age":21,
    "gender":"female",
    "blood_group":"B+"
}
try:
    print(dic["marks"])
except KeyError:
    print("Invalid index")
finally:
    print("end of code")

# 5.Create a calculator that handles invalid input and division by zero. Always print a thank-you message using finally.
print("Create a calculator that handles invalid input and division by zero. Always print a thank-you message using finally.")

try:
    num1=int(input("Enter the number : "))
    num2=int(input("Enter the number : "))
    div=print("Result : ",num1/num2)
except ZeroDivisionError:
    print("Can't possible ")

except ValueError:
    print("Please enter valid integers.")

finally:
    print("end of code")
