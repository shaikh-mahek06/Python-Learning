# 1.Return the sum of two numbers.
def add(a,b):
    return(a+b)

print("Addition is : ",add(4533,5433))

# 3.Return the square of a number.
def square(a):
    return(f"square of {a} is : {a*a}")

print(square(5))

# 4.Return the largest of three numbers.
def largest(a,b,c):
    return(max(a,b,c))

print("largest number is : ",largest(45,55,433))

# 5.Return the reverse of a string.
def reverse(string):
    rev_str=string[::-1]
    return ( rev_str)
print("reverse string is : ",reverse("life is full of blunders"))

# 6.Return whether a string is a palindrome.

def palindrome(string):
    if string[::]==string[::-1]:
        return True
    else:
        return False
    return

print(palindrome("madam"))

# 7.Return the factorial of a number.
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

# 8. Return the average of a list. 
print("8. Return the average of a list.")
def average(list):
    total=0
    for i in list:
        total+=i
    return total/len(list)
print(average([2,3,4]))
    