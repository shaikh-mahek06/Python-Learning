# 1.Divide two numbers. Print the result in the else block if successful, and always print a completion message using finally.
print("1.Write a program to divide two numbers. Display the result if possible. Print a message from the finally block.")
try:
    num1=int(input("Enter the number : "))
    num2=int(input("Enter the number : "))
    result=num1/num2
    
except ZeroDivisionError:
    print("Can't possible ")
else:
    print("Result : ",result)

finally:
    print("end of code")

# 2.Open a file. If it opens successfully, print its contents in else. Always close the file in finally.

try:
    file=open("data.txt")
except FileNotFoundError:
    print("File not found")
else:
    print("file founded")
finally:
    print("end of code")

# 3.Access a list element using an index entered by the user.

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    value = numbers[index]

except IndexError:
    print("Invalid Index.")

else:
    print("Element:", value)

finally:
    print("List operation completed.")