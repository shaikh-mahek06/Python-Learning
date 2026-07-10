# 1. Print numbers from 1 to N
def num(n):
    if n==0:
        return 
    num(n-1)
    print(n)

num(10)

#  2. Print numbers from N to 1
def numbers(n):
    if n==0:
        return
    print(n)
    numbers(n-1)

numbers(10)

# 3. Factorial
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# 4. Fibonacci
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))

# 5. Sum of first N numbers
def total(n):
    if n==0:
        return 0
    return n + total(n-1)

print(total(3))